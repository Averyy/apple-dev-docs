# resourceStatusForVersions:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Type Method

Check status for a set of resources.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```objc
+ (CNResourceStatus) resourceStatusForVersions:(NSSet<NSNumber *> *) resourceVersions;
```

## Return Value

The first encountered non-ready status, or CNResourceStatusReady if all are ready.

## Parameters

- `resourceVersions`: Resource version(s) to check. Empty set to check all available resource versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnassetinfo-8ja4t/resourcestatusforversions:)*