# backLeftButton(position:)

**Framework**: Game Controller  
**Kind**: method

Returns the name of the back left button at the specified location.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst ?+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
static func backLeftButton(position: Int) -> GCButtonElementName
```

#### Return Value

The name of the back left button.

## Parameters

- `position`: The relative position of the button to the other back left button. Pass   for the button nearest to the natural rest position of the person’s finger. Pass   for an additional button that requires the person to move their fingers to press if it exists.

## See Also

- [static func backRightButton(position: Int) -> GCButtonElementName](gcbuttonelementname-swift.struct/backrightbutton(position:).md)
  Returns the name of the back right button at the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcbuttonelementname-swift.struct/backleftbutton(position:))*