# CLSContext

**Framework**: ClassKit  
**Kind**: class  
**Role**: Class

An area of your app that represents an assignable task, like a quiz or a chapter.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CLSContext
```

```objc
@interface CLSContext : CLSObject
```

## Mentions

- [Creating bookmarks and assignments from your app](./creating-bookmarks-and-assignments-from-your-app.md)

#### Overview

Make it easy for teachers to understand the app content a context represents by configuring it with information like a clear, concise title localized for the regions that your app supports.

A context can contain groups of other contexts, like a book that contains chapters or a chapter that contains sections. You can assemble contexts into a hierarchy of up to eight levels that acts as a table of contents for teachers who want to assign your app content. See [Advertising your app’s assignable content](./advertising-your-app-s-assignable-content.md) for more details.

## Topics

### Creating contexts
- [init(type: CLSContextType, identifier: String, title: String)](./clscontext/init%28type,identifier,title%29.md)
  Initializes a new context.
- [class CLSObject](./clsobject.md)
  The abstract base class for objects managed by ClassKit.
### Identifying the context
- [var identifier: String](./clscontext/identifier.md)
  A string that uniquely identifies a context among its siblings.
- [var title: String](./clscontext/title.md)
  The name of the context as it appears to users.
- [var summary: String?](./clscontext/summary.md)
  An optional, user-visible description of the context.
- [var thumbnail: CGImage?](./clscontext/thumbnail.md)
  An optional thumbnail image associated with the context.
### Managing the context type
- [var type: CLSContextType](./clscontext/type.md)
  The kind of content a context represents.
- [func setType(CLSContextType)](./clscontext/settype%28_%29.md)
  Updates the kind of content that a context represents.
- [enum CLSContextType](./clscontexttype.md)
  The kinds of assignable content a context can contain.
- [var customTypeName: String?](./clscontext/customtypename.md)
  An optional name that the system presents to the user if you choose the custom context type.
### Characterizing the context
- [var suggestedAge: NSRange](./clscontext/suggestedage.md)
  The range of ages, measured in years, for which you deem a context’s content suitable.
- [var suggestedCompletionTime: NSRange](./clscontext/suggestedcompletiontime.md)
  A suggested time range to complete a task, measured in minutes.
- [var isAssignable: Bool](./clscontext/isassignable.md)
  A Boolean that indicates whether teachers can assign the context as a task.
### Managing context presentation
- [var displayOrder: Int](./clscontext/displayorder.md)
  The position of a context relative to its siblings.
- [var topic: CLSContextTopic?](./clscontext/topic.md)
  The area of study to which a context relates.
- [struct CLSContextTopic](./clscontexttopic.md)
  The areas of study to which contexts may relate.
### Indicating progress reporting capabilities
- [var progressReportingCapabilities: Set<CLSProgressReportingCapability>](./clscontext/progressreportingcapabilities.md)
  The kinds of progress reporting that the context can perform.
- [func addProgressReportingCapabilities(Set<CLSProgressReportingCapability>)](./clscontext/addprogressreportingcapabilities%28_%29.md)
  Adds a progress reporting capability to the set of capabilities for the context.
- [func resetProgressReportingCapabilities()](./clscontext/resetprogressreportingcapabilities%28%29.md)
  Resets the set of capabilities for the context.
- [class CLSProgressReportingCapability](./clsprogressreportingcapability.md)
  A progress reporting capability supported by a context.
### Activating and deactivating a context
- [Informing ClassKit that a task is about to begin](./informing-classkit-that-a-task-is-about-to-begin.md)
  Activate and deactivate contexts according to user interaction.
- [func becomeActive()](./clscontext/becomeactive%28%29.md)
  Tells a context to become the active context.
- [func resignActive()](./clscontext/resignactive%28%29.md)
  Tells a context to stop being the active context.
- [var isActive: Bool](./clscontext/isactive.md)
  A Boolean indicating whether the context is active.
### Creating activities
- [var currentActivity: CLSActivity?](./clscontext/currentactivity.md)
  The activity available for recording progress.
- [func createNewActivity() -> CLSActivity](./clscontext/createnewactivity%28%29.md)
  Creates and returns a new activity instance for the context.
### Managing context hierarchy
- [var identifierPath: [String]](./clscontext/identifierpath.md)
  The identifier path that locates the context within the data store’s context hierarchy.
- [var parent: CLSContext?](./clscontext/parent.md)
  The direct ancestor of this context.
- [func removeFromParent()](./clscontext/removefromparent%28%29.md)
  Removes the context from its parent.
- [func addChildContext(CLSContext)](./clscontext/addchildcontext%28_%29.md)
  Adds the specifed context as a child of the context receiving the method call.
- [func descendant(matchingIdentifierPath: [String], completion: (CLSContext?, (any Error)?) -> Void)](./clscontext/descendant%28matchingidentifierpath,completion%29.md)
  Finds the context with the given identifier path relative to this context.
### Creating a context presentation hierarchy
- [var navigationChildContexts: [CLSContext]](./clscontext/navigationchildcontexts.md)
  The child contexts that a user can navigate to from this context in the Schoolwork app.
- [func addNavigationChildContext(CLSContext)](./clscontext/addnavigationchildcontext%28_%29.md)
  Adds a child context that users can navigate to from this context.
- [func removeNavigationChildContext(CLSContext)](./clscontext/removenavigationchildcontext%28_%29.md)
  Removes the specified context as a presentable child of this context.
### Configuring deep links
- [Linking directly to assignments](./linking-directly-to-assignments.md)
  Make it easy for teachers to guide students to specific content.
- [var universalLinkURL: URL?](./clscontext/universallinkurl.md)
  A URL that leads to the content in your app associated with the current context.
- [var isClassKitDeepLink: Bool](../Foundation/nsuseractivity/isclasskitdeeplink.md)
  A Boolean value that indicates whether a user activity represents a ClassKit context.
- [var contextIdentifierPath: [String]?](../Foundation/nsuseractivity/contextidentifierpath.md)
  The identifier path associated with a user activity generated by an app that adopts ClassKit.

## Relationships

### Inherits From
- [CLSObject](./clsobject.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Contexts
- [Advertising your app’s assignable content](./advertising-your-app-s-assignable-content.md)
  Assemble a hierarchy of contexts and declare your app’s assignable content.
- [protocol CLSContextProvider](./clscontextprovider.md)
  An interface used to tell your ClassKit context provider app extension to update contexts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext)*