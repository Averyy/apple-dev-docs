# maximumRating

**Framework**: ManagedSettings  
**Kind**: property

The metadata associated with the maximum app rating setting.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
static let maximumRating: BoundedSettingMetadata<Int>
```

#### Discussion

Use `maximumRating` to access the metadata for [`maximumRating`](appstoresettings/maximumrating-swift.property.md). The default value is `1000` and the bounds are `0...2000`.

## See Also

- [var maximumRating: Int?](appstoresettings/maximumrating-swift.property.md)
  The maximum app rating the user can download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/appstoresettings/maximumrating-swift.type.property)*