# tabViewSearchActivation(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Configures the activation and deactivation behavior of search in the search tab.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
nonisolated
func tabViewSearchActivation(_ activation: TabSearchActivation) -> some View
```

#### Discussion

Use this modifier on a [`TabView`](../tabview.md) to change how search activation is handled. The exact activation behavior is determined by the [`TabSearchActivation`](../tabsearchactivation.md) you pass to this modifier:

```swift
struct TabExampleView: View {
    @State private var text: String = ""

    var body: some View {
        TabView {
            Tab("Books", systemImage: "book") {
                BooksTab()
            }
            Tab(role: .search) {
                NavigationStack {
                    SearchContent()
                }
            }
        }
        .searchable(text: $text)
        .tabViewSearchActivation(.searchTabSelection)
    }
}
```

By default, search is only activated and deactivated by the user.

## See Also

### Tab views
- [func defaultAdaptableTabBarPlacement(AdaptableTabBarPlacement) -> some View](./defaultadaptabletabbarplacement%28_%29.md)
  Specifies the default placement for the tabs in a tab view using the adaptable sidebar style.
- [func defaultTabBarPlacement(AdaptableTabBarPlacement) -> some View](./defaulttabbarplacement%28_%29.md)
  Specifies the preferred placement for the tabs of a [`TabView`](../tabview.md) in the [`sidebarAdaptable`](../tabviewstyle/sidebaradaptable.md) style on platforms where the tab bar cannot adapt between different representations, and only one representation can be shown.
- [func sectionActions<Content>(content: () -> Content) -> some View](./sectionactions%28content%29.md)
  Adds custom actions to a section.
- [func tabBarMinimizeBehavior(TabBarMinimizeBehavior) -> some View](./tabbarminimizebehavior%28_%29.md)
  Sets the behavior for tab bar minimization.
- [func tabViewBottomAccessory<Content>(content: () -> Content) -> some View](./tabviewbottomaccessory%28content%29.md)
  Places a view as the bottom accessory of the tab view.
- [func tabViewBottomAccessory<Content>(isEnabled: Bool, content: () -> Content) -> some View](./tabviewbottomaccessory%28isenabled,content%29.md)
  Places a view as the bottom accessory of the tab view. Use this modifier to dynamically show and hide the accessory view.
- [func tabViewCustomization(Binding<TabViewCustomization>?) -> some View](./tabviewcustomization%28_%29.md)
  Specifies the customizations to apply to the sidebar representation of the tab view.
- [func tabViewSidebarHeader<Content>(content: () -> Content) -> some View](./tabviewsidebarheader%28content%29.md)
  Adds a custom header to the sidebar of a tab view.
- [func tabViewSidebarFooter<Content>(content: () -> Content) -> some View](./tabviewsidebarfooter%28content%29.md)
  Adds a custom footer to the sidebar of a tab view.
- [func tabViewSidebarBottomBar<Content>(content: () -> Content) -> some View](./tabviewsidebarbottombar%28content%29.md)
  Adds a custom bottom bar to the sidebar of a tab view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/tabviewsearchactivation(_:))*