# descendant(matchingIdentifierPath:completion:)

**Framework**: ClassKit  
**Kind**: method

Finds the context with the given identifier path relative to this context.

**Availability**:
- iOS 11.4+
- iPadOS 11.4+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func descendant(matchingIdentifierPath identifierPath: [String]) async throws -> CLSContext
```

## Mentions

- [Recording student progress](recording-student-progress.md)
- [Declaring your app’s context hierarchy](declaring-your-app-s-context-hierarchy.md)
- [Building missing contexts](building-missing-contexts.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func descendant(matchingIdentifierPath identifierPath: [String]) async throws -> CLSContext
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

> ❗ **Important**:  ClassKit calls your completion handler on an arbitrary thread. If you need to do work on a particular thread from inside the handler, dispatch that work to the appropriate queue.

## Parameters

- `identifierPath`: The identifier path of the context to find, relative to the current context.
- `completion`: A closure the method calls with the found context, or   if none could be found, and an error indicating the reason for failure, if any.

## See Also

- [var identifierPath: [String]](clscontext/identifierpath.md)
  The identifier path that locates the context within the data store’s context hierarchy.
- [var parent: CLSContext?](clscontext/parent.md)
  The direct ancestor of this context.
- [func removeFromParent()](clscontext/removefromparent.md)
  Removes the context from its parent.
- [func addChildContext(CLSContext)](clscontext/addchildcontext(_:).md)
  Adds the specifed context as a child of the context receiving the method call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/descendant(matchingidentifierpath:completion:))*