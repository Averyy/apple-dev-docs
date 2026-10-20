# previewContext(faceColor:)

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Returns a view that Xcode can display as a preview.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
func previewContext(faceColor: CLKComplicationTemplate.PreviewFaceColor = .multicolor) -> some View
```

## Parameters

- `faceColor`: The tint color for the face. If you omit this parameter, it defaults to a full-color face. For a list of valid face colors, see [`CLKComplicationTemplate.PreviewFaceColor`](./previewfacecolor.md).

## See Also

### Displaying Previews
- [CLKComplicationTemplate.PreviewFaceColor](./previewfacecolor.md)
  The valid face colors for complication templates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplate/previewcontext(facecolor:))*