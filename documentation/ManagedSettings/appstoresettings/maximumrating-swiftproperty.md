# maximumRating

**Framework**: ManagedSettings  
**Kind**: property

The maximum app rating the user can download.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var maximumRating: Int? { get set }
```

#### Discussion

The value is `nil` if your app doesn’t constrain this setting. The following list provides U.S. rating descriptions for the levels:

- `1000` - All
- `600` - 17+
- `300` - 12+
- `200` - 9+
- `100` - 4+
- `0` - None

## See Also

- [static let maximumRating: BoundedSettingMetadata<Int>](appstoresettings/maximumrating-swift.type.property.md)
  The metadata associated with the maximum app rating setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/appstoresettings/maximumrating-swift.property)*