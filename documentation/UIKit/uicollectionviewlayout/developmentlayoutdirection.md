# developmentLayoutDirection

**Framework**: UIKit  
**Kind**: property

The direction of the language you used when designing your custom layout.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var developmentLayoutDirection: UIUserInterfaceLayoutDirection { get }
```

#### Discussion

The default value of this property is the layout direction used by the language associated with the main bundle’s development region. Subclasses may override this property and return a different value.

## See Also

- [var flipsHorizontallyInOppositeLayoutDirection: Bool](uicollectionviewlayout/flipshorizontallyinoppositelayoutdirection.md)
  A Boolean value that indicates whether the horizontal coordinate system is automatically flipped at appropriate times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/developmentlayoutdirection)*