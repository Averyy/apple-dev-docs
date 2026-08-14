---
url: https://developer.apple.com/design/human-interface-guidelines/search-fields
framework: HIG
---

# Search fields

**Type:** article

**Platforms:** ios, ipados, macos, tvos, visionos, watchos

> **Updated 2026-06-08:** Updated terminology and refined guidance for search as a tab in iOS.

A search field lets people search a collection of content for specific terms they enter.

![A stylized representation of a search field containing placeholder text and a dictation icon. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](/images/com.apple.HIG/components-search-field-intro~dark@2x.png)
A search field is an editable text field that displays a Search icon, a Clear button, and placeholder text where people can enter what they are searching for. Search fields can use a [Scope bars and tokens](search-fields.md#Scope-bars-and-tokens) as well as [Scope bars and tokens](search-fields.md#Scope-bars-and-tokens) to help filter and refine the scope of their search. Across each platform, there are different patterns for accessing search based on the goals and design of your app.
For developer guidance, see [Adding a search interface to your app](../swiftui/adding-a-search-interface-to-your-app.md); for guidance related to systemwide search, see [Searching](searching.md).

## Best practices
**Use placeholder text to help people know what they can search for.** Placeholder text can be helpful when you need to reinforce the scope of your search or to educate people about the type of content that search has access to.
**If possible, start search immediately when a person types.** Searching while someone types makes the search experience feel more responsive because it provides results that are continuously refined as the text becomes more specific.
**Consider showing suggested search terms.** For example, you can display recent searches before search begins, or predictive search suggestions as a person types. This can help someone search faster, even when the search itself doesn’t begin immediately.
**Simplify search results.** Provide the most relevant search results first to minimize the need for someone to scroll to find what they’re looking for. In addition to prioritizing the most likely results, consider categorizing them to help people find what they want.
**Consider letting people filter search results.** For example, you can include a scope bar in the search results content area to help people quickly and easily filter search results.

## Scope bars and tokens
Scope bars and tokens are components you can use to let someone narrow the parameters of a search either before or after they make it.
- A *scope bar* is a control for filtering and adjusting the scope of a search.
- A *token* is a visual representation of a search term that someone can select and edit, and acts as a filter for any additional terms in the search.
![A diagram of the Mail app on iPhone with the search field open above the keyboard and the word Design entered in the field. Callouts indicate a scope bar at the top of the screen to switch between searching all mailboxes and the current mailbox, and a list of tokens in a Suggestions area beneath the bar that represent different filters for the search.](/images/com.apple.HIG/search-fields-scope-control-tokens~dark@2x.png)
**Use a scope bar to filter among clearly defined search categories.** A scope bar can help someone move from a broader scope to a narrower one. For example, in Mail on iPhone, a scope bar helps people move from searching their entire mailbox to just the specific mailbox they’re viewing. For developer guidance, see [Scoping a search operation](../swiftui/scoping-a-search-operation.md).
**Default to a broader scope and let people refine it as they need.** A broader scope provides context for the full set of available results, which helps guide people in a useful direction when they choose to narrow the scope.
**Use tokens to filter by common search terms or items.** When you define a token, the term it represents gains a visual treatment that encapsulates it, indicating that people can select and edit it as a single item. Tokens can clarify a search term, like filtering by a specific contact in Mail, or focus a search to a specific set of attributes, like filtering by photos in Messages. For the related macOS component, see [Token fields](token-fields.md).
**Consider pairing tokens with search suggestions.** People may not know which tokens are available, so pairing them with search suggestions can help people learn how to use them.

## Platform considerations
*No additional considerations for visionOS*.

### iOS
There are three main places you can position the entry point for search:
- As a tab in a tab bar
- In a toolbar at the bottom or top of the screen
- Directly inline with content
Where search makes the most sense depends on the layout, content, and navigation of your app.

#### Search as a tab
You can place search as a tab in a tab bar, which keeps search visible and always available as people switch between the sections of your app. There are two styles of search tabs:
- **Standard tab.** This style displays the search tab uniformly with the rest of the tab bar. Tapping the search tab navigates people to a search landing page with a search field at the top.
- **Button appearance.** This style displays the search tab as a separate button and allows people to start searching immediately. Tapping the search tab brings focus to the search field and displays the keyboard.
![An illustration of a tab bar at the bottom of an iPhone screen. A tab for search appears as part of the tab bar.](/images/com.apple.HIG/search-fields-search-as-tab-standard~dark@2x.png)
![An illustration of a tab bar at the bottom of an iPhone screen. A tab for search appears on the trailing edge as a separate button.](/images/com.apple.HIG/search-fields-search-as-tab-prominent~dark@2x.png)
**Choose the standard tab style to provide suggestions, promote discovery, and encourage exploration.** This style of search tab creates a dedicated landing page for search, providing an opportunity to reveal any content or suggestions that might be helpful before someone taps the field to begin the search. This approach is great for an app with a variety of rich content that people might want to explore. For example, Apple TV uses this search tab style to present its various genres and categories, helping ground people in what’s available before they search.
**Choose the button appearance to help people quickly find what they need.** When someone interacts with this style of search tab, the keyboard immediately appears with the search field above it, ready to begin the search. This approach provides a more transient experience that brings people directly back to their previous tab after they exit search, and is ideal when you want search to resolve quickly and seamlessly.

#### Search in a toolbar
As an alternative to search in a tab bar, you can also place search in a toolbar either at the bottom or top of the screen.
- You can include search in a bottom toolbar either as an expanded field or as a toolbar button, depending on how much space is available. When someone taps it, it animates into a search field above the keyboard so they can begin typing.
- You can include search in a top toolbar, also called a navigation bar, where it appears as a toolbar button. When someone taps it, it animates into a search field that appears either above the keyboard or at the top if there isn’t space at the bottom.
![An illustration of an iPhone screen with search in a bottom toolbar. The search field is positioned in an isolated group between a Filter button on the leading edge and a Compose button on the trailing edge.](/images/com.apple.HIG/search-fields-ios-toolbar-with-items~dark@2x.png)
![An illustration of an iPhone screen with search in a top toolbar. A Back button appears on the leading edge, and an Add button appears on the trailing edge. A button group with Search and More appears next to the Add button.](/images/com.apple.HIG/search-fields-ios-navigation-bar-item~dark@2x.png)
**Place search at the bottom if there’s room.** You can either add a search field to an existing toolbar, or as a new toolbar where search is the only item. Search at the bottom is useful in any situation where search is a priority, since it keeps the search experience easy to reach. Examples of apps with search at the bottom in various toolbar layouts include Settings, where it’s the only item, and Mail and Notes, where it fits alongside other important controls.
**Place search at the top when itʼs important to defer to content at the bottom of the screen, or thereʼs no bottom toolbar.** Use search at the top in cases where covering the content might interfere with a primary function of the app. The Wallet app, for example, includes event passes in a stack at the bottom of the screen for easy access and viewing at a glance.

#### Search as an inline field
In some cases you might want your app to include a search field inline with content.
**Place search as an inline field when its position alongside the content it searches strengthens that relationship.** When you need to filter or search within a single view, it can be helpful to have search appear directly next to content to illustrate that the search applies to it, rather than globally. This pattern is useful if your app has more than one search field and if location plays a critical role in the scope of your search. For example, although the main search in the Music app is a tab, people can navigate to their library and use an inline search field to filter their songs and albums.
**When at the top, position an inline search field above the list it searches, and consider pinning it to the top toolbar when scrolling.** This helps keep it distinct from search that appears in other locations.

### iPadOS, macOS
The placement and behavior of the search field in iPadOS and macOS is similar. If your app is available on both iPad and Mac, try to keep the search experience as consistent as possible across both platforms.
![An illustration of an iPad screen with a search field on the trailing edge of the top toolbar. The search field has the word Design entered into the field, and three search suggestions appear in a list beneath the field.](/images/com.apple.HIG/search-fields-toolbar-search-ipad~dark@2x.png)
![An illustration of a Mac screen with a search field on the trailing edge of the toolbar. The search field has the word Design entered into the field, and three search suggestions appear in a list beneath the field.](/images/com.apple.HIG/search-fields-toolbar-search-mac~dark@2x.png)
**Put a search field at the trailing side of the toolbar for many common uses.** Many apps benefit from the familiar pattern of search in the toolbar, particularly apps with split views that need to search across multiple columns of information, like Mail, Notes, and Voice Memos. This placement makes great use of space because it lets people navigate results while keeping their selection visible in the detail view. Additionally, consider placing search in the toolbar if results appear in the detail view of your app, like in Freeform, where search in the toolbar filters the boards in the detail view below.
**Include search at the top of the sidebar when filtering content or navigation there.** Apps such as Settings take advantage of search to quickly filter the sidebar and expose sections that may be multiple levels deep, providing a simple way for people to search, preview, and navigate to the section or setting they’re looking for. This approach is useful if your app has a rich detail view and you need to create a distinct separation between the sidebar you’re filtering and the adjacent view.
![An illustration of an iPad screen with a search field at the top of the sidebar on the leading edge of the screen.](/images/com.apple.HIG/search-fields-ipad-search-in-sidebar~dark@2x.png)
**Include search as an item in the sidebar or tab bar when you want an area dedicated to discovery.** If your search is paired with rich suggestions, categories, or content that needs more space, it can be helpful to have a dedicated area for it. This is particularly useful for apps where browsing and search go hand in hand, like Music and TV, where it provides a unified location to highlight suggested content, categories, and recent searches. A dedicated area also ensures search is always available as people navigate and switch sections of your app.
![An illustration of an iPad screen with a tab bar at the top edge. The trailing side of the tab bar includes a Search tab with a distinct background color to differentiate it from other tab areas.](/images/com.apple.HIG/search-fields-ipad-search-in-tab-bar~dark@2x.png)
**In a search field in a dedicated area, consider immediately focusing the field when a person navigates to the area to help them search faster and locate the field more easily.** An exception to this is on iPad when only a virtual keyboard is available, in which case it’s better to leave the field unfocused to prevent the keyboard from unexpectedly covering the view.
**Account for window resizing with the placement of the search field.** On iPad, the search field fluidly resizes with the app window like it does on Mac. However, for compact views on iPad, itʼs important to ensure that search is available where it’s most contextually useful. For example, Notes and Mail place search above the column for the content list when they resize down to a compact view.

### tvOS
A search screen is a specialized keyboard screen that helps people enter search text, displaying search results beneath the keyboard in a fully customizable view. For developer guidance, see [UISearchController](../uikit/uisearchcontroller.md).
![An illustration of a search screen in tvOS. The screen includes a field with a keyboard input area at the top, a scope bar, and a grid of top results at the bottom.](/images/com.apple.HIG/search-fields-tvos-search@2x.png)
**Provide suggestions to make searching easier.** People typically don’t want to do a lot of typing in tvOS. To improve the search experience, provide popular and context-specific search suggestions, including recent searches when available. For developer guidance, see [Using suggested searches with a search controller](../uikit/using-suggested-searches-with-a-search-controller.md).

### watchOS
When someone taps the search field, the system displays a text-input control that covers the entire screen. The app only returns to the search field after they tap the Cancel or Search button.

## Resources

#### Related
[Searching](searching.md)
[Token fields](token-fields.md)

#### Developer documentation
[Adding a search interface to your app](../swiftui/adding-a-search-interface-to-your-app.md) — SwiftUI
[searchable(text:placement:prompt:)](../swiftui/view/searchable(text:placement:prompt:).md) — SwiftUI
[UISearchBar](../uikit/uisearchbar.md) — UIKit
[UISearchTextField](../uikit/uisearchtextfield.md) — UIKit
[NSSearchField](../appkit/nssearchfield.md) — AppKit

#### Videos
- [Design intuitive search experiences](https://developer.apple.com/videos/play/wwdc2026/292) - Explore new patterns and best practices when implementing search in your app. Discover how search plays a key role in helping people find and navigate content, and find out how to integrate search across different navigation models and Apple platforms.
- [Get to know the new design system](https://developer.apple.com/videos/play/wwdc2025/356) - Dive deeper into the new design system to explore key changes to visual design, information architecture, and core system components. Learn how the system reshapes the relationship between interface and content, enabling you to create designs that are dynamic, harmonious, and consistent across devices, screen sizes, and input modes.
- [Discoverable design](https://developer.apple.com/videos/play/wwdc2021/10126) - Discover how you can create interactive, memorable experiences to onboard people into your app. We’ll take you through discoverable design practices and learn how you can craft explorable, fun interfaces that help people grasp the possibilities of your app at a glance. We’ll also show you how to apply this methodology to personalize your content and make your app easy to customize.

## Change log
| Date | Changes |
| --- | --- |
| June 8, 2026 | Updated terminology and refined guidance for search as a tab in iOS. |
| June 9, 2025 | Updated guidance for search placement in iOS, consolidated iPadOS and macOS platform considerations, and added guidance for tokens. |
| September 12, 2023 | Combined guidance common to all platforms. |
| June 5, 2023 | Added guidance for using search fields in watchOS. |




---
*Source: [https://developer.apple.com/design/human-interface-guidelines/search-fields](https://developer.apple.com/design/human-interface-guidelines/search-fields)*
