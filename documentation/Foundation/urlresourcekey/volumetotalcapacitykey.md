# volumeTotalCapacityKey

**Framework**: Foundation  
**Kind**: property

Key for the volume’s total capacity in bytes (read-only).

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let volumeTotalCapacityKey: URLResourceKey
```

#### Discussion

> ❗ **Important**:  This API has the potential of being misused to access device signals to try to identify the device or user, also known as fingerprinting. Regardless of whether a user gives your app permission to track, fingerprinting is not allowed. When you use this API in your app or third-party SDK (an SDK not provided by Apple), declare your usage and the reason for using the API in your app or third-party SDK’s `PrivacyInfo.xcprivacy` file. For more information, including the list of valid reasons for using the API, see [`Describing use of required reason API`](https://developer.apple.com/documentation/BundleResources/describing-use-of-required-reason-api).

## See Also

- [Checking Volume Storage Capacity](checking-volume-storage-capacity.md)
  Confirm that you have enough local storage space for a large amount of data.
- [static let volumeAvailableCapacityKey: URLResourceKey](urlresourcekey/volumeavailablecapacitykey.md)
  Key for the volume’s available capacity in bytes (read-only).
- [static let volumeAvailableCapacityForImportantUsageKey: URLResourceKey](urlresourcekey/volumeavailablecapacityforimportantusagekey.md)
  Key for the volume’s available capacity in bytes for storing important resources (read-only).
- [static let volumeAvailableCapacityForOpportunisticUsageKey: URLResourceKey](urlresourcekey/volumeavailablecapacityforopportunisticusagekey.md)
  Key for the volume’s available capacity in bytes for storing nonessential resources (read-only).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcekey/volumetotalcapacitykey)*