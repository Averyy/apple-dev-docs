# init(rating:maximumRating:title:detail:)

**Framework**: CarPlay  
**Kind**: init

Creates a rating item with a current and a maximum rating.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init(rating: NSNumber?, maximumRating: NSNumber?, title: String?, detail: String?)
```

## Parameters

- `rating`: A number in the range of 0 to  . The number must be an increment of 0.5.
- `maximumRating`: A whole number in the range of 1 to 5 that specifies the maximum rating that the item allows.
- `title`: The text that the template displays as the item’s title.
- `detail`: The text that the template displays below or beside the title, depending on the template’s layout. See   for more information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinformationratingitem/init(rating:maximumrating:title:detail:))*