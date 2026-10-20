# UIBackgroundModes

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

Services provided by an app that require it to run in the background.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- visionOS 1.0+
- watchOS 4.0+

## Details

- **Name**: `UIBackgroundModes` (Required background modes)
- **Type**: array of string 

## Possible Values

- `audio`
- `bluetooth-central`
- `bluetooth-peripheral`
- `external-accessory`
- `fetch`
- `location`
- `nearby-interaction`
- `network-authentication`
- `newsstand-content`
- `processing`
- `push-to-talk`
- `remote-notification`
- `screen-capture`
- `voip`

#### Discussion

To add this key to your Information Property List, enable the Background Modes capability in Xcode. For information on configuring background execution modes and the platforms that support them, see [Configuring background execution modes](../../Xcode/configuring-background-execution-modes.md).

## See Also

### Background execution
- [WKBackgroundModes](./wkbackgroundmodes.md)
  The services a watchOS app provides that require it to continue running in the background.
- [BGTaskSchedulerPermittedIdentifiers](./bgtaskschedulerpermittedidentifiers.md)
  An array of strings containing developer-specified task identifiers in reverse URL notation.
- [LSBackgroundOnly](./lsbackgroundonly.md)
  A Boolean value indicating whether the app runs only in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uibackgroundmodes)*