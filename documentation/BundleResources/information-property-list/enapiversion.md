# ENAPIVersion

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A number that specifies the version of the API to use.

**Availability**:
- iOS 13.7+
- iPadOS 13.7+

## Details

- **Name**: `ENAPIVersion`
- **Type**: number

## Possible Values

- `1`: Use version 1 of the API.
- `2`: Use version 2 of the API.



**Default**: `1`

#### Discussion

> ❗ **Important**:  This type is available in iOS 12.5, and in iOS 13.7 and later.

iOS 13.7 introduces a new method to calculate the user’s Exposure Risk Value, described in [`ENExposureConfiguration`](../../ExposureNotification/enexposureconfiguration.md). Set this value to `2` to use this new version and its calculation method, or set this value to `1` to use the earlier API and its calculation method. If you don’t explicitly set this value, the default is `1`.

## See Also

### Exposure notification
- [ENDeveloperRegion](./endeveloperregion.md)
  A string that specifies the region that the app supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/enapiversion)*