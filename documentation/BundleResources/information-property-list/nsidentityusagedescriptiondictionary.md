# NSIdentityUsageDescriptionDictionary

**Framework**: Bundle Resources  
**Kind**: dictionary

A dictionary that contains messages that explain why your app is requesting identity information.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- visionOS 1.0+



**Type**: dictionary

#### Discussion

Use this key when you have multiple scenarios for requesting identity information from a person. Provide a description string for each use case, and key each entry with a string that you define. For example, if your app needs age verification for one feature and identity verification for another, use a separate dictionary entry for each purpose. In each description string, describe the reason the feature requires identity information.

The following image shows two description strings that use `NSIdentityUsageDescriptionDictionary`.

![A screenshot of the NSIdentityUsageDescriptionDictionary item in the Xcode property list editor showing two entries. The first entry has the key age-verification and a value that reads, Checks your age to make sure you’re old enough to drive. The second entry has the key identity-verification and a value that reads, Verifies your identity before you can rent a car.](/images/com.apple.bundleresources/NSIdentityUsageDescriptionDictionary-image@2x.png)

> **Note**: The dictionary allows up to 5 entries, and each usage description string allows up to 256 characters.

For more information about requesting identity information, see [`Requesting identity data from a Wallet pass`](https://developer.apple.com/documentation/passkit/requesting-identity-data-from-a-wallet-pass). For design guidance, see [`Human Interface Guidelines > Technologies > Wallet`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/technologies/wallet#identity-verification).

## See Also

- [NSFinancialDataUsageDescription](information-property-list/nsfinancialdatausagedescription.md)
  A message that tells people why the app is requesting access to financial data stored in Wallet.
- [NSIdentityUsageDescription](information-property-list/nsidentityusagedescription.md)
  A message that tells people why the app is requesting identity information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsidentityusagedescriptiondictionary)*