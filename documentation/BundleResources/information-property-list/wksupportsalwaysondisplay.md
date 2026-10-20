# WKSupportsAlwaysOnDisplay

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that determines whether the system displays the app in the Always On state.

**Availability**:
- watchOS 8.0+

## Details

- **Name**: `WKSupportsAlwaysOnDisplay` (App Supports Always On Display (Watch))
- **Type**: boolean



**Default**: `YES`

#### Discussion

If [`true`](../../Swift/true.md), the system displays the app in the Always On state when the app is the frontmost app or running an active background session. Apps compiled for watchOS 8 and later have Always On enabled by default; however, users can disable Always On for the entire device or on a per-app basis by selecting Settings > Display & Brightness > Always On.

For more information, see `Designing Your App for the Always On State`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/wksupportsalwaysondisplay)*