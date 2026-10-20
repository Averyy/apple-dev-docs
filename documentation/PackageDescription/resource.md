# Resource

**Framework**: PackageDescription  
**Kind**: struct  
**Role**: Structure

A resource to bundle with the Swift package.

**Availability**:
- SwiftPM 5.3+

## Declaration

```swift
struct Resource
```

#### Overview

If a Swift package declares a Swift tools version of 5.3 or later, it can include resource files. Similar to source code, Swift Package Manager scopes resources to a target, so you must put them into the folder that corresponds to the target they belong to. For example, any resources for the `MyLibrary` target must reside in `Sources/MyLibrary`. Use subdirectories to organize your resource files in a way that simplifies file identification and management. For example, put all resource files into a directory named `Resources`, so they reside at `Sources/MyLibrary/Resources`.

By default, Swift Package Manager handles common resources types for Apple platforms automatically. For example, you don’t need to declare XIB files, storyboards, Core Data file types, and asset catalogs as resources in your package manifest. However, you must explicitly declare other file types — for example, image files — as resources using the [`process(_:localization:)`](./resource/process%28_,localization%29.md) or [`copy(_:)`](./resource/copy%28_%29.md) rules. Alternatively, exclude resource files from a target by passing them to the target initializer’s [`exclude`](./target/exclude.md) parameter.

To learn more about package resources, see [Bundling resources as a Swift Package](../Xcode/bundling-resources-with-a-swift-package.md).

## Topics

### Applying Rules
- [static func process(String, localization: Resource.Localization?) -> Resource](./resource/process%28_,localization%29.md)
  Applies a platform-specific rules to the resource at the given path.
- [Resource.Localization](./resource/localization.md)
  Defines the explicit type of localization for resources.
- [static func copy(String) -> Resource](./resource/copy%28_%29.md)
  Applies the copy rule to a resource at the given path.
- [static func embedInCode(String) -> Resource](./resource/embedincode%28_%29.md)
  Applies the embed rule to a resource at the given path.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring File Locations
- [var path: String?](./target/path.md)
  The path of the target, relative to the package root.
- [var exclude: [String]](./target/exclude.md)
  The paths to source and resource files that you don’t want to include in the target.
- [var sources: [String]?](./target/sources.md)
  The source files in this target.
- [var resources: [Resource]?](./target/resources.md)
  The explicit list of resource files in the target.
- [var publicHeadersPath: String?](./target/publicheaderspath.md)
  The path to the directory that contains public headers of a C-family target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/resource)*