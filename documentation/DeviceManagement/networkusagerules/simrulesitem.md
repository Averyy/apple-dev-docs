# NetworkUsageRules.SIMRulesItem

**Framework**: Device Management  
**Kind**: dictionary

The policy for individual SIM cards.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
object NetworkUsageRules.SIMRulesItem
```

## Properties

- `ICCIDs` ([string]) *(required)*: One or more ICCIDs of SIM cards for which the `WiFiAssistPolicy` applies. All ICCIDs in all installed Network Usage Rules payloads must be unique. An example ICCID is `89310410106543789301`.
- `WiFiAssistPolicy` (integer) *(required)*: The Wi-Fi Assist policy to apply to the SIM cards specified in the ICCIDs. Allowed values: - `2`: Use the default system policy for the specified SIM card(s).
- `3`: Make Wi-Fi Assist switch more aggressively from a poor Wi-Fi connection to cellular data for the specified SIM card(s). This setting may increase cellular data use and may impact battery life. For more information, see [`About Wi-Fi Assist`](https://developer.apple.comhttps://support.apple.com/en-us/HT205296).

## See Also

- [object NetworkUsageRules.ApplicationRulesItem](networkusagerules/applicationrulesitem.md)
  The application rules dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkusagerules/simrulesitem)*