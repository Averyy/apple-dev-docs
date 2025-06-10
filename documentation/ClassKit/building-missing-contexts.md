# Building missing contexts

**Framework**: ClassKit

Create and initialize missing contexts.

#### Overview

When you request a context with a call to the [`descendant(matchingIdentifierPath:completion:)`](clscontext/descendant(matchingidentifierpath:completion:).md) method, whether because you are declaring it or because you want to do something with it, the data store returns the context indicated by the identifier path. But if that context or any of its ancestors doesn’t already exist, the data store asks its delegate to create new ones.

##### Adopt the Data Store Delegate Protocol

To enable the delegate to create a context, you adopt the [`CLSDataStoreDelegate`](clsdatastoredelegate.md) protocol in your app.

```swift
// Extension to MyClass for adopting the data store delegate protocol.
extension MyClass: CLSDataStoreDelegate {

    // Call this once at app launch.
    func setupClassKit() {
        CLSDataStore.shared.delegate = self
    }

    // The delegate callback for creating new contexts.
    func createContext(forIdentifier identifier: String, parentContext: CLSContext, parentIdentifierPath: [String]) -> CLSContext? {
        let identifierPath = parentIdentifierPath + [identifier]
        
        let object = <# A model object based on identifierPath #>
        let context = CLSContext(type: object.contextType, identifier: identifier, title: object.title)
        
        return context
    }
}
```

The data store uses the delegate callback to ask for each new context it encounters. You use the identifier path to determine exactly what the new context should look like. A good way to do this is to map the identifier path to a model object you already have and use its properties to inform context creation. For example, your model objects might represent books, chapters, sections, and quizzes, all of which implement a `title` parameter suitable for use on the context. By also storing a `contextType` parameter on each model instance, with values like [`CLSContextType.book`](clscontexttype/book.md), [`CLSContextType.chapter`](clscontexttype/chapter.md), [`CLSContextType.section`](clscontexttype/section.md), or [`CLSContextType.quiz`](clscontexttype/quiz.md), you can create contexts based entirely on model instances, as shown above.

##### Provide Descriptive Titles

The title you provide at context initialization is what teachers see when browsing your content in the Schoolwork app. Make it easy for teachers to understand what your app offers by choosing good context titles and localizing them, as appropriate. Because titles are the most visible aspect of your hierarchy, it’s important that you make them both clear and descriptive. The title “Thermodynamics Quiz” is much more self-explanatory than “Quiz 8” for example.

##### Optionally Indicate Display Order

If appropriate, provide guidance for ordering your contexts using the [`displayOrder`](clscontext/displayorder.md) property. For example, immediately after instantiating a context that represents a chapter, you might indicate its position as the chapter number:

```swift
if let chapter = object as? Chapter {
    context.displayOrder = chapter.number
}
```

##### Classify Contexts By Subject

You can further classify a context with an optional topic using one of the values from [`CLSContextTopic`](clscontexttopic.md), like [`math`](clscontexttopic/math.md) or [`socialScience`](clscontexttopic/socialscience.md). For apps covering a variety of different subject matters, topics help teachers differentiate between the various parts of your app. An app that has a singular focus can simply set its top-level context to the topic that best matches that subject. For example, for a book reader:

```swift
dataStore.mainAppContext.topic = .literacyAndWriting
```

##### Return the Context

Once you create and configure the context, you simply return it to the data store. The data store associates the context with the appropriate parent and keeps it in memory. The next time you ask the data store for that context, it returns the previously generated one instead of requesting a new one from the delegate. Additionally, for a user logged in as a teacher, the data store saves the changes to an internal database that’s shared with the Schoolwork app and synchronized over iCloud. This allows the context to persist even across launches of your app, but only for teachers. For privacy reasons, other users don’t record contexts in the database.

> **Note**:  It’s possible to build a context hierarchy without using the delegate protocol by initializing [`CLSContext`](clscontext.md) instances and manually assigning them as children of other contexts, starting with the app’s main context at the root. But a context hierarchy might already exist in the local data store from a previous launch of your app. Rebuilding generates needless network traffic while the updates are synchronized through iCloud. By using a data store delegate, you only create new contexts when they aren’t already in the data store.

## See Also

- [var delegate: (any CLSDataStoreDelegate)?](clsdatastore/delegate.md)
  The data store delegate instance.
- [protocol CLSDataStoreDelegate](clsdatastoredelegate.md)
  An interface the data store uses to request new contexts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/building-missing-contexts)*