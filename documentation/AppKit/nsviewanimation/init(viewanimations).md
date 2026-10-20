# init(viewAnimations:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns an `NSViewAnimation` object initialized with the supplied information.

**Availability**:
- macOS

## Declaration

```swift
init(viewAnimations: [[NSViewAnimation.Key : Any]])
```

```objc
- (instancetype) initWithViewAnimations:(NSArray<NSDictionary<NSString *,id> *> *) viewAnimations;
```

#### Return Value

The created `NSViewAnimation` object or `nil` if there was a problem initializing the object.

## Parameters

- `viewAnimations`: An array of [`NSDictionary`](../../Foundation/nsdictionary.md) objects. Each dictionary specifies a view or window to animate and the effect to apply. `viewAnimations` can be `nil`, but you must later set the required array of dictionaries with [`viewAnimations`](./viewanimations.md) if you want to use the capabilities of the `NSViewAnimation` class. See`View Animation Dictionary Keys` for a description of valid keys and values for dictionaries in `viewAnimations`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewanimation/init(viewanimations:))*