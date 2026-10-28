# Enhancing your app’s content with tab navigation

**Framework**: SwiftUI  
**Role**: Sample Code  
**Download**: [DestinationVideo.zip](https://docs-assets.developer.apple.com/published/3248dcf174b4/DestinationVideo.zip)

Keep your app content front and center while providing quick access to navigation using the tab bar.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Overview

[Destination Video](../visionOS/destination-video.md) adopts the [`sidebarAdaptable`](./tabviewstyle/sidebaradaptable.md) tab view style, which optimizes the content browsing experience for each platform.

Starting in iPadOS 18, the tab bar appears on the top of the screen floating over your content instead of appearing at the bottom of the screen. This appearance creates an immersive full-screen browsing experience. Tab bars provide people with access to the top-level navigation in your app. However, too many tabs can make it hard for people to locate content. Implementing a sidebar makes it easier to navigate a detailed information hierarchy.

[Video: A screen recording of Destination Video on iPad that shows the tab bar turning into a sidebar, then becoming editable.](https://developer.apple.com/tutorials/videos/com.apple.SwiftUI/Enhancing-your-app-content-with-tab-navigation-hero-video.mp4)

### Create a tab bar

You can create a [`TabView`](./tabview.md) with an explicit selection binding using the [`init(selection:content:)`](./tabview/init%28selection,content%29.md) initializer. To add a tab within a `TabView` initialize a [`Tab`](./tab.md). Destination Video uses the [`init(_:systemImage:value:content:)`](./tab/init%28_,systemimage,value,content%29.md) initializer to create each tab:

```swift
@State private var selectedTab: Tabs = .watchNow

var body: some View {
    TabView(selection: $selectedTab) {
        Tab("Watch Now", systemImage: "play", value: .watchNow) {
            WatchNowView()
        }
        // More tabs...
    }
}
```

The selection value type of the `TabView` matches the value type of the tabs it contains. In this case, the value of each `Tab` is of type `Tabs`, which this sample defines the following enumeration:

```swift
enum Tabs: Equatable, Hashable, Identifiable {
    case watchNow
    case library
    case new
    case favorites
    case search
}
```

> **Note**: When using symbol images for your tabs, use the outline variant. The system automatically selects the filled variant when it appears in a tab bar.

![A screenshot of the iPadOS tab bar in Simulator. The tab bar is highlighted, the tab bar has an icon on the left that turns it into a sidebar, followed by the tabs: Watch Now, Library, New, Favorites, and Search, which appears as a magnifying glass.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/Enhancing-your-app-content-with-tab-navigation-create-tab@2x.png)

Additionally, this sample uses the [`search`](./tabrole/search.md) role with the [`init(value:role:content:)`](./tab/init%28value,role,content%29.md) initializer. Setting the tab role to `search` makes the system applies a few default customizations to the `Tab`. The search tab gets:

- The default title for search, “search”
- The default system symbol for search, a magnifying glass
- The default pinned behavior for search, the system automatically pins it in the tab bar

```swift
Tab(value: .search, role: .search) {
    // ...
}
```

Pinned tabs appear at the trailing edge of the tab bar, depending on the preferred language of your app. When the language is a left-to-right language, they appear on the right side. When the language is a right-to-left language, they’re on the left side.

![A screenshot of the tab bar with the a search tab highlighted.  The tab bar has an icon on the left that turns it into a sidebar, followed by the tabs: Watch Now, Library, New, Favorites, and Search, which appears as a magnifying glass.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/Enhancing-your-app-content-with-tab-navigation-search@2x.png)

### Build hierarchy in tab view

You can use a [`TabSection`](./tabsection.md) to declare a secondary tab hierarchy within a `TabView`. For example Destination Video uses the [`init(content:header:)`](./tabsection/init%28content,header%29.md) initializer to create tab sections.

```swift
TabView(selection: $selectedTab) {
    Tab("Watch Now", systemImage: "play", value: .watchNow) {
        WatchNowView()
    }

    // More tabs...
    
    TabSection {
        Tab("Cinematic Shots", systemImage: "list.and.film", value: .collections(.cinematic)) {
            // ...
        }
    } header: {
        Label("Collections", systemImage: "folder")
    }
}
```

Then it extends the `Tabs` enumeration to account for secondary tabs:

```swift
enum Tabs: Equatable, Hashable, Identifiable {
    case watchNow
    // ..
    case search
    case collections(Category)
    case animations(Category)
}

enum Category: Equatable, Hashable, Identifiable, CaseIterable {
    case cinematic
    case forest
    case sea
    // ...
}
```

This sample uses a [`ForEach`](./foreach.md) loop to iterate and initialize a new `Tab` for each tab value.

```swift
TabSection {
    ForEach(Category.collectionsList) { collection in
        Tab(collection.name, systemImage: collection.icon, value: Tabs.collections(collection)) {
            // ..
        }
    }
} header: {
    Label("Collections", systemImage: "folder")
}
```

### Make the tab bar adaptable

Tab bars with the [`sidebarAdaptable`](./tabviewstyle/sidebaradaptable.md) style allow people to toggle between the sidebar and tab bar. This lets your app leverage the convenience of being able to quickly navigate to top-level destinations within a compact tab bar while providing rich navigation hierarchy and destination options in the sidebar.

To create an adaptable tab bar, Destination Video adds the [`tabViewStyle(_:)`](./view/tabviewstyle%28_%29.md) modifier to its `TabView` and passes in the value [`sidebarAdaptable`](./tabviewstyle/sidebaradaptable.md).

```swift
TabView(selection: $selectedTab) {
    // Tabs
    // ..
}
.tabViewStyle(.sidebarAdaptable)

```

A `TabView` with the `sidebarAdaptable` style appears differently depending on the platform, as shown in the following images.

**iPadOS**:

[Video: A video that shows a tab bar morphing into a sidebar on iPad.](https://developer.apple.com/tutorials/videos/com.apple.SwiftUI/Enhancing-your-app-content-with-tab-navigation-section-video.mp4)
A `TabView` appears as top tab bar that becomes a sidebar in iPadOS. Tab sections appear in both the sidebar and the tab bar. In compact view, a `TabView` appears as a bottom tab bar.

**iOS**:

[Video: A screenshot of tab view on iOS.](https://developer.apple.com/tutorials/videos/com.apple.SwiftUI/Enhancing-your-app-content-with-tab-navigation-iOS-section-video.mp4)
A `TabView` appears as a bottom tab bar in iOS. Secondary tabs appear in the tab bar. Unlike iPadOS, the section header doesn’t appear in the tab bar.

**macOS**:

![A screenshot of tab view on macOS](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/Enhancing-your-app-content-with-tab-navigation-macOS@2x.png)

**tvOS**:

[Video: A video that shows tab view on tvOS.](https://developer.apple.com/tutorials/videos/com.apple.SwiftUI/Enhancing-your-app-content-with-tab-navigation-tvOS-video.mp4)
A `TabView` appears as a sidebar that collapses into a floating pill after a person selects a tab in tvOS. Tab sections appear in the sidebar.

**visionOS**:

[Video: An image that shows tab view on visionOS.](https://developer.apple.com/tutorials/videos/com.apple.SwiftUI/Enhancing-your-app-content-with-tab-navigation-visionOS-section-video.mp4)
A `TabView` appears as an ornament in visionOS. Tab section headers appear in the ornament. If you select a tab section header in the ornament, the sidebar displays the tabs in that section.

> **Note**: By default, contents in a `ScrollView(.horizontal)` scroll under the sidebar when you use the `sidebarAdaptable` tab view style in iPadOS. You can prevent the content from scrolling under the sidebar by adding the [`clipped(antialiased:)`](./view/clipped%28antialiased%29.md) or [`clipShape(_:style:)`](./view/clipshape%28_,style%29.md) modifier to `ScrollView`.

### Enable customization

Tab view customization allows people to enter edit mode and personalize the tab bar. The customization in Destination Video allows people to:

- Drag and drop tabs to remove and add tabs to the tab bar
- Hide non-essential tabs
- Reorder tabs in tab sections in the sidebar
- Reorder tabs in the tab bar

To enable customizations, this sample defines a [`TabViewCustomization`](./tabviewcustomization.md) and attaches it to the `TabView` using the [`tabViewCustomization(_:)`](./view/tabviewcustomization%28_%29.md) modifier. To persist the customization, this sample adds [`AppStorage`](./appstorage.md) with an identifier for a  `TabViewCustomization` variable. Finally, it adds the [`customizationID(_:)`](./tabcontent/customizationid%28_%29.md) modifier to each tab.

```swift
@AppStorage("sidebarCustomizations") var tabViewCustomization: TabViewCustomization
@State private var selectedTab: Tabs = .watchNow

var body: some View {
    TabView(selection: $selectedTab) {
        Tab("Watch Now", systemImage: "play", value: .watchNow) {
            WatchNowView()
        }
        .customizationID(Tabs.watchNow.customizationID)

        // More tabs...

    }
    .tabViewCustomization($tabViewCustomization)
}
```

To keep the most important tabs visible and in a fixed position, turn off customization behavior for those tabs using the [`customizationBehavior(_:for:)`](./tabcontent/customizationbehavior%28_,for%29.md) modifier.

```swift
Tab("Watch Now", systemImage: "play", value: .watchNow) {
    WatchNowView()
}
.customizationBehavior(.disabled, for: .sidebar, .tabBar)
```

![A screenshot of a tab view in edit mode on iPad.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/Enhancing-your-app-content-with-tab-navigation-customization@2x.png)

### Set the default visibility for tabs

In iPadOS, if there are too many tabs to fit in the screen, the system collapses the tabs that don’t fit and enables scrolling. However, having too many tabs can make it harder for people to locate the tab they’re looking for and navigate your app. Consider limiting the number of tabs so they all fit in the tab bar. The [`defaultVisibility(_:for:)`](./tabcontent/defaultvisibility%28_,for%29.md) modifier sets the default visibility of a `Tab` or `TabSection`.

Destination Video contains five tabs and two tab sections, each tab section contains multiple secondary tabs, but only seven tabs appear in the tab bar. In order to limit the tab bar to the most important tabs, all tabs within a `TabSection` are hidden from the tab bar by default.

```swift
TabSection {
    // Tabs
} header {
    // Section header
}
.defaultVisibility(.hidden, for: .tabBar)
```

**iPadOS**:

[Video: A video that shows a tab bar morphing into a sidebar on iPad.](https://developer.apple.com/tutorials/videos/com.apple.SwiftUI/Enhancing-your-app-content-with-tab-navigation-iPadOS-video.mp4)

**iOS**:

![A screenshot of tab view on iOS.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/Enhancing-your-app-content-with-tab-navigation-iOS@2x.png)

**macOS**:

![A screenshot of tab view on macOS](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/Enhancing-your-app-content-with-tab-navigation-macOS@2x.png)

**tvOS**:

[Video: A video that shows tab view on tvOS.](https://developer.apple.com/tutorials/videos/com.apple.SwiftUI/Enhancing-your-app-content-with-tab-navigation-tvOS-video.mp4)

**visionOS**:

![An image that shows tab view on visionOS.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/Enhancing-your-app-content-with-tab-navigation-visionOS.png)

If you enable customization, the [`defaultVisibility(_:for:)`](./tabcontent/defaultvisibility%28_,for%29.md) modifier still allows people to drag a tab from the sidebar into the tab bar. If you want to restrict tabs to only appear in the sidebar use [`sidebarOnly`](./tabplacement/sidebaronly.md) instead of setting the default visibility.

For design guidance, see Human Interface Guidelines >  [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars).

## See Also

#### Related samples

- [Destination Video](../visionOS/destination-video.md)
  Leverage SwiftUI to build an immersive media experience in a multiplatform app.

#### Related articles

- [Elevating your iPad app with a tab bar and sidebar](../UIKit/elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md)
  Provide a compact, ergonomic tab bar for quick access to key parts of your app, and a sidebar for in-depth navigation.

#### Related videos

- [Elevate your tab and sidebar experience in iPadOS](https://developer.apple.com/videos/play/wwdc2024/10147)
  iPadOS 18 introduces a new navigation system that gives people the flexibility to choose between using a tab bar or sidebar. The newly redesigned tab bar provides more space for content and other functionality. Learn how to use SwiftUI and UIKit to enable customization features – like adding, removing and reordering tabs – to enable a more personal touch in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/enhancing-your-app-content-with-tab-navigation)*