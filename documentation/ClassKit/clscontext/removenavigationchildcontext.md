# removeNavigationChildContext(_:)

**Framework**: ClassKit  
**Kind**: method

Removes the specified context as a presentable child of this context.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
func removeNavigationChildContext(_ child: CLSContext)
```

#### Discussion

Use this method to remove a child from the [`navigationChildContexts`](clscontext/navigationchildcontexts.md) collection of a given context. This only affects presentation. The method doesn’t alter your app’s context hierarchy because it has no effect on the context’s [`identifierPath`](clscontext/identifierpath.md).

## Parameters

- `child`: The context that you want to remove as a presentable child of this context.

## See Also

- [var navigationChildContexts: [CLSContext]](clscontext/navigationchildcontexts.md)
  The child contexts that a user can navigate to from this context in the Schoolwork app.
- [func addNavigationChildContext(CLSContext)](clscontext/addnavigationchildcontext(_:).md)
  Adds a child context that users can navigate to from this context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/removenavigationchildcontext(_:))*