# CFURLBookmarkCreationOptions

**Framework**: Core Foundation  
**Kind**: struct  
**Role**: Structure

Type for bookmark data creation options.

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
struct CFURLBookmarkCreationOptions
```

```c
enum CFURLBookmarkCreationOptions : CFOptionFlags;
```

## Overview

See [Bookmark Data Creation Options](./bookmark-data-creation-options.md) for possible values.

## Topics

### Initializers
- [init(rawValue: CFOptionFlags)](./cfurlbookmarkcreationoptions/init%28rawvalue%29.md)
### Type Properties
- [static var minimalBookmarkMask: CFURLBookmarkCreationOptions](./cfurlbookmarkcreationoptions/minimalbookmarkmask.md)
  Specifies that an alias created with the bookmark data be created with minimal information, which may make it smaller but still able to resolve in certain ways.
- [static var preferFileIDResolutionMask: CFURLBookmarkCreationOptions](./cfurlbookmarkcreationoptions/preferfileidresolutionmask.md)
  Specifies that an alias created with the bookmark data prefers resolving with its embedded file ID.
- [static var securityScopeAllowOnlyReadAccess: CFURLBookmarkCreationOptions](./cfurlbookmarkcreationoptions/securityscopeallowonlyreadaccess.md)
  When combined with the [`withSecurityScope`](./cfurlbookmarkcreationoptions/withsecurityscope.md) option, specifies that you want to create a security-scoped bookmark that, when resolved, provides a security-scoped URL allowing read-only access to a file-system resource; for use in an app that adopts App Sandbox.
- [static var suitableForBookmarkFile: CFURLBookmarkCreationOptions](./cfurlbookmarkcreationoptions/suitableforbookmarkfile.md)
  Specifies that the bookmark data include properties required to create Finder alias files.
- [static var withSecurityScope: CFURLBookmarkCreationOptions](./cfurlbookmarkcreationoptions/withsecurityscope.md)
  Specifies that you want to create a security-scoped bookmark that, when resolved, provides a security-scoped URL allowing read/write access to a file-system resource; for use in an app that adopts App Sandbox.
- [static var withoutImplicitSecurityScope: CFURLBookmarkCreationOptions](./cfurlbookmarkcreationoptions/withoutimplicitsecurityscope.md)

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
- [typealias CFURLBookmarkFileCreationOptions](./cfurlbookmarkfilecreationoptions.md)
  Type for bookmark file creation options.
- [struct CFURLBookmarkResolutionOptions](./cfurlbookmarkresolutionoptions.md)
  Type for bookmark data resolution options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions)*