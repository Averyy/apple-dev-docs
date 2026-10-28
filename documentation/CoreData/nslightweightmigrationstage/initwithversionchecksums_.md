# initWithVersionChecksums:

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Creates a lightweight migration stage with the specified version checksums.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
- (instancetype) initWithVersionChecksums:(NSArray<NSString *> *) versionChecksums;
```

## Return Value

An initialized lightweight migration manager, or `nil` if Core Data can’t create one.

## Discussion

To determine an object model’s version checksum, use its [`versionChecksum`](../nsmanagedobjectmodel/versionchecksum.md) property. Alternatively, you can find the checksum in the versioned model’s `VersionInfo.plist` file or in Xcode’s build log.

## Parameters

- `versionChecksums`: The array of version checksums.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nslightweightmigrationstage/initwithversionchecksums:)*