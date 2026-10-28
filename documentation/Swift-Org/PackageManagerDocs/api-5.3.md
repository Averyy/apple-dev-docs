---
url: "https://docs.swift.org/latest/documentation/packagemanagerdocs/5.3"
framework: "Swift-Org/PackageManagerDocs"
---

# SwiftPM 5.3 Release Notes

**Framework**: Swift-Org/PackageManagerDocs  
**Role**: Article

SwiftPM brings several new features in version 5.3, all of which are opt-in based on the tools-version.

### Conditional dependencies

You can now declare conditions for a Swift package’s target dependencies, such as limiting the dependencies by platform. This gives you more flexibility to describe complex target dependencies that support multiple platforms. (40237402)

```swift
// swift-tools-version:5.3

import PackageDescription

let package = Package(
    name: "SamplePackage",
    dependencies: [
        .package(url: "https://github.com/pureswift/bluetooth", .branch("main")),
        .package(url: "https://github.com/pureswift/bluetoothlinux", .branch("main")),
    ],
    targets: [
        .target(
            name: "SampleExecutable",
            dependencies: [
                .product(name: "Bluetooth", condition: .when(platforms: [.macOS])),
                .product(name: "BluetoothLinux", condition: .when(platforms: [.linux])),
            ]
        ),
     ]
)
```

### Resources

Swift packages can now contain resources such as images, asset catalogs, storyboards, and other files. When Xcode builds an app that depends on a package, it adds the package’s code and resources to the app bundle for use at runtime. For more information see [Bundling Resources with a Swift Package](https://developer.apple.com/documentation/swift_packages/bundling_resources_with_a_swift_package). (54361843)

Any resource in the package can now contain localized content. In addition to localized content in asset catalogs, Xcode supports separate localization files in .lproj folders. For more information see [Localizing Package Resources](https://developer.apple.com/documentation/swift_packages/localizing_package_resources). (56925255)

**Important**: The addition of resource support also changed the inclusion behavior for non-source files in packages. Updating a package tools-version to 5.3, means one has to explicitly declare whether to exclude or process any file whose type is unknown to SwiftPM. This can be done at the file or directory level.

### Binary dependencies

Swift packages can now vend prebuilt libraries distributed as XCFrameworks, allowing dependencies on libraries that can’t be distributed as source code. When Xcode builds an app that uses such a package, it embeds the libraries into the app bundle. For more information see [Distributing Binary Frameworks as Swift Packages](https://developer.apple.com/documentation/swift_packages/distributing_binary_frameworks_as_swift_packages). (56592977)

## See Also

- [SwiftPM 6.4 Release Notes](./api-6.4.md)
  Swift Package Manager 6.4 makes Swift Build the new default build system, providing a unified build experience across all platforms Swift supports. This release also adds first-class support for generating Software Bill of Materials (SBOM) documents.
- [SwiftPM 6.3 Release Notes](./api-6.3.md)
- [SwiftPM 5.9 Release Notes](./api-5.9.md)
- [SwiftPM 5.8 Release Notes](./api-5.8.md)
- [SwiftPM 5.7 Release Notes](./api-5.7.md)
- [SwiftPM 5.6 Release Notes](./api-5.6.md)
- [SwiftPM 5.5 Release Notes](./api-5.5.md)
- [SwiftPM 5.4 Release Notes](./api-5.4.md)
  SwiftPM 5.4 includes several improvements, all of which are opt-in based on specifying a tools version of 5.4.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packagemanagerdocs/5.3)*