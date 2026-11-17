# init(handler:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a button and sets its action to the provided handler.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init(handler: ((CPNowPlayingButton) -> Void)? = nil)
```

```objc
- (instancetype) initWithHandler:(void (^)(CPNowPlayingButton *)) handler;
```

## Return Value

An initialized button.

## Discussion

When you instantiate a concrete subclass of [`CPNowPlayingButton`](../cpnowplayingbutton.md), use this initializer to specify the code to run when someone interacts with the button.

## Parameters

- `handler`: The handler to run when someone interacts with the button. This closure takes the button as a parameter and returns no value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingbutton/init(handler:))*