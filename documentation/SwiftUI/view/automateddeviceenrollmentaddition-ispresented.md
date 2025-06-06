# automatedDeviceEnrollmentAddition(isPresented:)

**Framework**: SwiftUI  
**Kind**: method

Presents a modal view that enables users to add devices to their organization.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
@MainActor
@preconcurrency func automatedDeviceEnrollmentAddition(isPresented: Binding<Bool>) -> some View
```

#### Return Value

The modal view that the system presents to the user.

#### Discussion

Use this view modifier to present UI in your app for device administrators to add devices purchased outside of the official channel to their organization — Apple School Manager, Apple Business Manager, or Apple Business Essentials. The system requires sign in with a Managed Apple Account that includes device enrollment privileges.

The following code example shows one way to present this view to your users:

Example Usage:

```swift
import SwiftUI
import AutomatedDeviceEnrollment

struct ContentView: View {
    @State private var isAddingDevices: Bool = false

    var body: some View {
        Button("Add Devices to Automated Device Enrollment") {
            isAddingDevices = true
        }
        .automatedDeviceEnrollmentAddition(isPresented: $isAddingDevices)
        .onChange(of: isAddingDevices) {
            if !isAddingDevices {
                // Handle dismiss action
            }
        }
    }
}
```

## Parameters

- `isPresented`: A binding to a Boolean value that determines whether to present the view.

## See Also

- [func managedContentStyle(ManagedContentStyle) -> some View](view/managedcontentstyle(_:).md)
  Applies a managed content style to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/automateddeviceenrollmentaddition(ispresented:))*