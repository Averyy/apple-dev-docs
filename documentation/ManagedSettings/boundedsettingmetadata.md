# BoundedSettingMetadata

**Framework**: ManagedSettings  
**Kind**: struct

Additional information about a bounded setting.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
struct BoundedSettingMetadata<Value> where Value : Comparable
```

## Topics

### Getting Metadata
- [let bounds: ClosedRange<Value>](boundedsettingmetadata/bounds.md)
  The range of values that a setting can accomodate.
- [let defaultValue: Value](boundedsettingmetadata/defaultvalue.md)
  The implicit value for a setting if your app doesn’t set a value.

## See Also

- [struct SettingMetadata](settingmetadata.md)
  Additional information about a configurable setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/boundedsettingmetadata)*