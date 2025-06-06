# ENAPIVersion

**Framework**: Bundle Resources  
**Kind**: typealias

A number that specifies the version of the API to use.

**Availability**:
- iOS 13.7+
- iPadOS 13.7+

#### Discussion

> ❗ **Important**:  This type is available in iOS 12.5, and in iOS 13.7 and later.

 This type is available in iOS 12.5, and in iOS 13.7 and later.

iOS 13.7 introduces a new method to calculate the user’s Exposure Risk Value, described in [`ENExposureConfiguration`](https://developer.apple.com/documentation/ExposureNotification/ENExposureConfiguration). Set this value to `2` to use this new version and its calculation method, or set this value to `1` to use the earlier API and its calculation method. If you don’t explicitly set this value, the default is `1`.

## See Also

- [ENDeveloperRegion](information-property-list/endeveloperregion.md)
  A string that specifies the region that the app supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/enapiversion)*