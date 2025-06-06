# previewDevice(_:)

**Framework**: Journaling Suggestions  
**Kind**: method

Overrides the device for a preview.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func previewDevice(_ value: PreviewDevice?) -> some View
```

#### Return Value

A preview that uses the given device.

#### Discussion

By default, Xcode automatically chooses a preview device based on your currently selected run destination. If you want to choose a device that doesn’t change based on Xcode settings, provide a `PreviewDevice` instance that you initialize with the name or model of a specific device:

```None
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
            .previewDevice(PreviewDevice(rawValue: "iPad Pro (11-inch)"))
    }
}
```

You can get a list of supported preview device names, like “iPhone 11”, “iPad Pro (11-inch)”, and “Apple Watch Series 5 - 44mm”, by using the `xcrun` command in the Terminal app:

```None
% xcrun simctl list devicetypes
```

Additionally, you can use the following values for macOS platform development:

- “Mac”
- “Mac Catalyst”

## Parameters

- `value`: A device to use for preview, or   to let Xcode   automatically choose a device based on the run destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/previewdevice(_:))*