# CFURLBookmarkResolutionOptions

**Framework**: Core Foundation  
**Kind**: struct

Type for bookmark data resolution options.

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
struct CFURLBookmarkResolutionOptions
```

#### Overview

See [`Bookmark Data Resolution Options`](bookmark-data-resolution-options.md) for possible values.

## Topics

### Initializers
- [init(rawValue: CFOptionFlags)](cfurlbookmarkresolutionoptions/init(rawvalue:).md)
### Type Properties
- [static var cfBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions](cfurlbookmarkresolutionoptions/cfbookmarkresolutionwithoutmountingmask.md)
  Specifies that no volume should be mounted during resolution of the bookmark data.
- [static var cfBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions](cfurlbookmarkresolutionoptions/cfbookmarkresolutionwithoutuimask.md)
  Specifies that no UI feedback accompany resolution of the bookmark data.
- [static var cfurlBookmarkResolutionWithSecurityScope: CFURLBookmarkResolutionOptions](cfurlbookmarkresolutionoptions/cfurlbookmarkresolutionwithsecurityscope.md)
  Specifies that the security scope, applied to the bookmark when it was created, should be used during resolution of the bookmark data.
- [static var cfurlBookmarkResolutionWithoutImplicitStartAccessing: CFURLBookmarkResolutionOptions](cfurlbookmarkresolutionoptions/cfurlbookmarkresolutionwithoutimplicitstartaccessing.md)
- [static var cfurlBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions](cfurlbookmarkresolutionoptions/cfurlbookmarkresolutionwithoutmountingmask.md)
- [static var cfurlBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions](cfurlbookmarkresolutionoptions/cfurlbookmarkresolutionwithoutuimask.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct CFURLBookmarkCreationOptions](cfurlbookmarkcreationoptions.md)
  Type for bookmark data creation options.
- [typealias CFURLBookmarkFileCreationOptions](cfurlbookmarkfilecreationoptions.md)
  Type for bookmark file creation options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkresolutionoptions)*