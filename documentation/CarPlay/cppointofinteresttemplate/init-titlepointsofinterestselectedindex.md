# init(title:pointsOfInterest:selectedIndex:)

**Framework**: CarPlay  
**Kind**: init

Creates a Point of Interest template with a title, the points of interest to display, and the initial selection’s index.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init(title: String, pointsOfInterest: [CPPointOfInterest], selectedIndex: Int)
```

#### Discussion

`pointsOfInterest` can contain a maximum of twelve points of interest because that is the most the template displays.

## Parameters

- `title`: The scrollable picker’s title.
- `pointsOfInterest`: An array that contains the points of interest the template displays.
- `selectedIndex`: The initial selection’s index. This is the array’s index for the specific point of interest you want to select. Use   to indicate no initial selection.

## See Also

- [class CPPointOfInterest](cppointofinterest.md)
  An object that describes a point of interest on the template’s map and in its scrollable picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppointofinteresttemplate/init(title:pointsofinterest:selectedindex:))*