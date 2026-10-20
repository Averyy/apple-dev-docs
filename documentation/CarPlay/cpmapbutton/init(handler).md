# init(handler:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a new map button.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(handler: ((CPMapButton) -> Void)? = nil)
```

```objc
- (instancetype) initWithHandler:(void (^)(CPMapButton *mapButton)) handler;
```

#### Return Value

A newly initialized map button.

## Parameters

- `handler`: The block invoked after the user taps the map button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmapbutton/init(handler:))*