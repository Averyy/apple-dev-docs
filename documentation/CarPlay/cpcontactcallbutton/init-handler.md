# init(handler:)

**Framework**: CarPlay  
**Kind**: init

Creates a button that invokes a handler when the user taps it.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init(handler: ((CPButton) -> Void)? = nil)
```

#### Return Value

A new contact directions button that invokes its handler when the user taps it.

#### Discussion

The button displays a system image that communicates its function.

## Parameters

- `handler`: The closure that the button invokes when the user taps it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpcontactcallbutton/init(handler:))*