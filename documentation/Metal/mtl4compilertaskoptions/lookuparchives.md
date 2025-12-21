# lookupArchives

**Framework**: Metal  
**Kind**: property

An array of archive instances that can potentially accelerate a compilation task.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var lookupArchives: [any MTL4Archive]? { get set }
```

#### Discussion

The compiler can reduce the runtime of a compilation task if it finds an entry that matches a function description within any of the archives in this array. The compiler searches the archives in the order of the array’s element.

Consider adding archives to the array in scenarios that can benefit from the runtime savings, such as repeat builds or when your app can share compilation results across multiple contexts.

> ❗ **Important**: Only add [`MTL4Archive`](mtl4archive.md) instances to the array that are compatible with the Metal device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compilertaskoptions/lookuparchives)*