# ManagedPackageView

**Framework**: ManagedAppDistribution  
**Kind**: struct

A view that displays information and controls for a managed software package.

**Availability**:
- macOS 26.4+

## Declaration

```swift
@MainActor
@preconcurrency struct ManagedPackageView
```

#### Overview

`ManagedPackageView` provides an interface for presenting managed packages in your app, displaying package details, installation status, and management controls in a consistent way across macOS and macCatalyst applications.

```swift
import SwiftUI
import ManagedAppDistribution

struct PackageListView: View {
    let packages: [ManagedPackage]

    var body: some View {
        List(packages) { package in
            ManagedPackageView(package: package)
        }
    }
}
```

## Topics

### Initializers
- [init(package: ManagedPackage)](managedpackageview/init(package:).md)
  Create a managed packaged view from a managed package.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedpackageview)*