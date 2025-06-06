# contentStyle

**Framework**: CarPlay  
**Kind**: property

The content style that the vehicle selects.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var contentStyle: CPContentStyle { get }
```

#### Discussion

The vehicle selects the content style according to the ambient light level. Your navigation app can use this value to determine the most appropriate style of map content to draw in its base view. The content style is independent of the user interface style, which controls light and dark mode.

## See Also

- [struct CPContentStyle](cpcontentstyle.md)
  The types of content style that the vehicle allows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsessionconfiguration/contentstyle)*