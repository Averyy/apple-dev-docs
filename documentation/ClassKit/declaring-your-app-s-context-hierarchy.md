# Declaring your app’s context hierarchy

**Framework**: Classkit

Tell ClassKit about your context hierarchy so teachers can see your assignable content.

#### Overview

After you design a context hierarchy for your app, tell ClassKit about it to make your app’s assignable content available to teachers in Apple’s Schoolwork app.

##### Assign a Unique Identifier to Each Context

Begin by giving each context a string identifier that’s unique among its siblings. For example, the chapters of a book might have the identifiers `chapter-1`, `chapter-2`, `chapter-3` and so on. This enables you to position each context within the hierarchy using an array of string identifiers—an —that traces exactly one route from an ancestor context to one of its descendants.

Identifiers only need to be unique among contexts with the same parent. So you might declare a `section-2` context for each of `chapter-1` and `chapter-2` because the complete identifier path uniquely identifies each section. But you can only declare one `section-2` context for a given chapter.

The identifiers don’t require a particular format because they aren’t ever displayed to a user. For example, if your chapter model happens to store a universally unique identifier in a [`UUID`](https://developer.apple.com/documentation/Foundation/UUID) instance, you can use the [`uuidString`](https://developer.apple.com/documentation/foundation/uuid/1779712-uuidstring) property to obtain a suitable identifier string for the corresponding context. As the name implies, the identifier is guaranteed to be unique (more than strictly necessary because it’s universally unique). And because you already keep the UUID with the chapter instance, you can easily look up the identifier when you need it.

##### Declare Each Leaf Context

Next declare the existence of each context at the edge of your hierarchy by asking ClassKit for it, using its identifier path to call the [`descendant(matchingIdentifierPath:completion:)`](clscontext/descendant(matchingidentifierpath:completion:).md) method. For example, to declare a context corresponding to a particular section in a book, you request it with the identifier path `["my-textbook", "chapter-1", "section-2"]`:

```swift
let context = CLSDataStore.shared.mainAppContext
context.descendant(matchingIdentifierPath: ["my-textbook",
                                            "chapter-1",
                                            "section-2"]) { _, _ in }
```

This method call is the same one you would use to retrieve the context to do something with it, but for the purposes of declaration, you can ignore the context returned as an argument to the trailing closure. Instead, you only make this call to indicate the existence of the `section-2` context, plus its ancestors `chapter-1` and `my-textbook`. Each is taken to be the child of the context that comes before it in the array, with the first context as the child of the context receiving the method call, in this case the main app context.

The above call declares a single context, but you can generalize this approach to declare your entire context hierarchy. For example, to declare the contexts for an entire book, just request the contexts for each section. This explicitly declares the sections, and implicity declares all of the chapters and the book itself.

```swift
let book = <# A Book instance #>
let context = CLSDataStore.shared.mainAppContext

for chapter in book.chapters {
    for section in chapter.sections {
        context.descendant(matchingIdentifierPath: [book.identifier,
                                                    chapter.identifier,
                                                    section.identifier]) { _, _ in }
    }
}
```

##### Declare Contexts Early

It’s important to declare the entire context hierarchy early in your app’s lifecycle, typically from within [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:didFinishLaunchingWithOptions:)). If you have dynamic material, such as new game levels that the user downloads long after first running your app, declare that additional content as soon as you know about it.

You use these declarations to advertise your app’s assignable content to Apple’s Schoolwork app, which is where teachers go to create assignments. Until a teacher’s instance of your app has performed context declaration on their own device, the teacher’s view of Schoolwork won’t offer your app’s content for assignments.

> **Note**:  In Schoolwork, teachers can browse assignable contexts, and assign them to students. Students only see the contexts in Schoolwork once they are assigned by a teacher.

## See Also

- [Building missing contexts](building-missing-contexts.md)
  Create and initialize missing contexts.
- [Informing ClassKit that a task is about to begin](informing-classkit-that-a-task-is-about-to-begin.md)
  Activate and deactivate contexts according to user interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ClassKit/declaring-your-app-s-context-hierarchy)*