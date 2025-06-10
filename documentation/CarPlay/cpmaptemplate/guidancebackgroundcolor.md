# guidanceBackgroundColor

**Framework**: CarPlay  
**Kind**: property

The background color the map template uses when displaying guidance.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var guidanceBackgroundColor: UIColor { get set }
```

#### Discussion

The system determines whether [`guidanceBackgroundColor`](cpmaptemplate/guidancebackgroundcolor.md) meets contrast requirements, and uses the default color when the provided color doesn’t meet those requirements. The system adjusts font color to correspond with the guidance background color.

> **Note**:  The system ignores alpha values.

## See Also

- [var automaticallyHidesNavigationBar: Bool](cpmaptemplate/automaticallyhidesnavigationbar.md)
  A Boolean value that indicates whether the template should automatically hide the navigation bar.
- [var hidesButtonsWithNavigationBar: Bool](cpmaptemplate/hidesbuttonswithnavigationbar.md)
  A Boolean value that tells the system to hide the map buttons when hiding the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/guidancebackgroundcolor)*