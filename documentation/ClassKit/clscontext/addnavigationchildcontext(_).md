# addNavigationChildContext(_:)

**Framework**: ClassKit  
**Kind**: method  
**Role**: Instance Method

Adds a child context that users can navigate to from this context.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
func addNavigationChildContext(_ child: CLSContext)
```

```objc
- (void) addNavigationChildContext:(CLSContext *) child;
```

## Discussion

Use this method to add a child to the [`navigationChildContexts`](./navigationchildcontexts.md) collection of a given context. This only affects presentation. The method doesn’t alter your app’s context hierarchy because it has no effect on the context’s [`identifierPath`](./identifierpath.md).

## Parameters

- `child`: A context that you want to add as a presentable child from this context.

## See Also

### Creating a context presentation hierarchy
- [var navigationChildContexts: [CLSContext]](./navigationchildcontexts.md)
  The child contexts that a user can navigate to from this context in the Schoolwork app.
- [func removeNavigationChildContext(CLSContext)](./removenavigationchildcontext%28_%29.md)
  Removes the specified context as a presentable child of this context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/addnavigationchildcontext(_:))*