# init(_:action:)

**Framework**: CoreLocationUI  
**Kind**: init

Creates a location button with the specified title and action.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
init(_ title: LocationButton.Title? = .currentLocation, action: @escaping () -> Void)
```

## Parameters

- `title`: The text that the button displays. For possible values, see  .
- `action`: The action that initiates every time the user taps the button.

## See Also

- [LocationButton.Title](locationbutton/title.md)
  Constants that specify the text of a button title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocationui/locationbutton/init(_:action:))*