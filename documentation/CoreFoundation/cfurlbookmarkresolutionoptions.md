# CFURLBookmarkResolutionOptions

**Framework**: Core Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum CFURLBookmarkResolutionOptions : CFOptionFlags;
```

## Overview

See [Bookmark Data Resolution Options](./bookmark-data-resolution-options.md) for possible values.

## Topics

### Initializers
- [init(rawValue: CFOptionFlags)](./cfurlbookmarkresolutionoptions/init%28rawvalue%29.md)
### Type Properties
- [static var cfBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions](./cfurlbookmarkresolutionoptions/cfbookmarkresolutionwithoutmountingmask.md)
  Specifies that no volume should be mounted during resolution of the bookmark data.
- [static var cfBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions](./cfurlbookmarkresolutionoptions/cfbookmarkresolutionwithoutuimask.md)
  Specifies that no UI feedback accompany resolution of the bookmark data.
- [static var cfurlBookmarkResolutionWithSecurityScope: CFURLBookmarkResolutionOptions](./cfurlbookmarkresolutionoptions/cfurlbookmarkresolutionwithsecurityscope.md)
  Specifies that the security scope, applied to the bookmark when it was created, should be used during resolution of the bookmark data.
- [static var cfurlBookmarkResolutionWithoutImplicitStartAccessing: CFURLBookmarkResolutionOptions](./cfurlbookmarkresolutionoptions/cfurlbookmarkresolutionwithoutimplicitstartaccessing.md)
- [static var cfurlBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions](./cfurlbookmarkresolutionoptions/cfurlbookmarkresolutionwithoutmountingmask.md)
- [static var cfurlBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions](./cfurlbookmarkresolutionoptions/cfurlbookmarkresolutionwithoutuimask.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Bookmark Data Types
- [struct CFURLBookmarkCreationOptions](./cfurlbookmarkcreationoptions.md)
  Type for bookmark data creation options.
- [typealias CFURLBookmarkFileCreationOptions](./cfurlbookmarkfilecreationoptions.md)
  Type for bookmark file creation options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkresolutionoptions)*