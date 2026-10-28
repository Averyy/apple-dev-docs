# remove(_:)

**Framework**: ClassKit  
**Kind**: method  
**Role**: Instance Method

Marks a context for removal.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func remove(_ context: CLSContext)
```

```objc
- (void) removeContext:(CLSContext *) context;
```

## Discussion

If your context hierarchy changes, either because your app’s content is dynamic, or as a result of an app update, you might need to remove old contexts from the data store. Call this method to mark a context for removal. Call the [`save(completion:)`](./save%28completion%29.md) method to commit the change.

When you remove a context, the framework removes all of its decendants as well.

## Parameters

- `context`: The context to remove.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsdatastore/remove(_:))*