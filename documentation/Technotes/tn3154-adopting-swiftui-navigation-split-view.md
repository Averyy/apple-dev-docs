# TN3154: Adopting SwiftUI navigation split view

**Framework**: Technotes

Use navigation split view to enable two and three column navigation in your SwiftUI app while maintaining compatibility with earlier OS versions.

#### Overview

[`NavigationSplitView`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/navigationsplitview) is a view that presents views in two or three columns, where selections in leading columns control presentations in subsequent columns. The Navigation split view API is available on iOS 16, macOS 13, tvOS 16, watchOS 9 and visionOS 1.

Transition from the deprecated [`NavigationView`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/navigationview) API if your app has a minimum deployment target of at least iOS 16, macOS 13, tvOS 16, watchOS 9 or visionOS 1. For more information, see [`Migrating to new navigation types`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/migrating-to-new-navigation-types).

This document describes how using a custom wrapper makes it easier to adopt `NavigationSplitView` and ensures your app remains compatible with the deprecated `NavigationView`, without increasing the app deployment target.

#### Using Api Availability Check to Provide Backward Compatibility Using a Custom Wrapper

Use the `#available()` keyword to execute code conditionally based on required platform and version. This allows your app use `NavigationSplitView` if the specified OS versions are iOS 16, macOS 13, tvOS 16, watchOS 9 or visionOS 1 while supporting `NavigationView` for earlier OS versions.

To ensure backward compatibility on earlier versions of iOS, macOS, tvOS and watchOS, create and use a custom wrapper view that conditionally uses either `NavigationSplitView` or `NavigationView` depending on the availability of the API. For apps that use one column navigation view, consider using [`NavigationStack`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/navigationstack).

```swift
struct NavigationSplitViewWrapper<Sidebar, Content, Detail>: View where Sidebar: View, Content: View, Detail: View {
    private var sidebar: Sidebar
    private var content: Content
    private var detail: Detail
    
    init(
        @ViewBuilder sidebar: () -> Sidebar,
        @ViewBuilder content: () -> Content,
        @ViewBuilder detail:  () -> Detail
    ) {
        self.sidebar = sidebar()
        self.content = content()
        self.detail = detail()
    }
    
    var body: some View {
        if #available(iOS 16, macOS 13, tvOS 16, watchOS 9, visionOS 1, *) {
            // Use the latest API available
            NavigationSplitView {
                sidebar
            } content: {
                content
            } detail: {
                detail
            }
        } else {
            // Alternative code for earlier versions of OS.
            NavigationView {
                // The first column is the sidebar.
                sidebar
                
                // Initial content of the second column.
                content
                
                // Initial content for the third column.
                detail
            }
            .navigationViewStyle(.columns)
        }
    }
}
```

> **Note**: Navigation split view collapses all of its columns into a stack and shows the last column that displays useful information for [`compact size classes`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/layout), such as on iPhone or in iPad’s Slide Over mode. It also collapses all of its columns into a stack on Apple Watch and Apple TV, regardless of the size class.

#### Revision History

- **2023-08-29** First published.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3154-adopting-swiftui-navigation-split-view)*