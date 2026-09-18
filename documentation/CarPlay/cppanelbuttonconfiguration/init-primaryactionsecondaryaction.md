# init(primaryAction:secondaryAction:)

**Framework**: CarPlay  
**Kind**: init

Initializes the button configuration object with the specified buttons.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
init(primaryAction: CPTextButton, secondaryAction: CPTextButton?)
```

#### Return Value

An initialized panel button configuration object.

## Parameters

- `primaryAction`: The primary button for the panel. Use this button to specify the default or primary action someone might want to perform. The initializer makes a copy of the provided button.
- `secondaryAction`: The secondary button for the panel. Use this to specify an additional action someone might want to perform. The initializer makes a copy of the provided button, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppanelbuttonconfiguration/init(primaryaction:secondaryaction:))*