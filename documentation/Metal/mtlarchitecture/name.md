# name

**Framework**: Metal  
**Kind**: property

The name of a GPU device’s architecture.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var name: String { get }
```

#### Discussion

The property’s value is equivalent to the output from the `metal-arch` command line tool on the same system.

```shell
% xcrun metal-arch
applegpu_g13s
```

Apps can use this property’s value to make decisions at runtime. For example, an app could retrieve a GPU-specific file from its developer’s content delivery network (CDN), such as a shader library or binary archive. See [`Shader Libraries`](shader-libraries.md) and [`Shader Library and Archive Creation`](shader-library-and-archive-creation.md) for more information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlarchitecture/name)*