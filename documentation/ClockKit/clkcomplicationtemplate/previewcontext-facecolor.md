# previewContext(faceColor:)

**Framework**: ClockKit  
**Kind**: method

Returns a view that Xcode can display as a preview.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
func previewContext(faceColor: CLKComplicationTemplate.PreviewFaceColor = .multicolor) -> some View
```

## Parameters

- `faceColor`: The tint color for the face. If you omit this parameter, it defaults to a full-color face. For a list of valid face colors, see  .

## See Also

- [CLKComplicationTemplate.PreviewFaceColor](clkcomplicationtemplate/previewfacecolor.md)
  The valid face colors for complication templates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplate/previewcontext(facecolor:))*