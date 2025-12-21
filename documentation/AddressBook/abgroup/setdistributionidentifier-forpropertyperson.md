# setDistributionIdentifier(_:forProperty:person:)

**Framework**: Address Book  
**Kind**: method

Assigns a specific distribution identifier for a person’s multivalue list property so that the group can be used as a distribution list.

**Availability**:
- macOS ?+

## Declaration

```swift
func setDistributionIdentifier(_ identifier: String!, forProperty property: String!, person: ABPerson!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if successful; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

The default distribution identifier is a multivalue list’s primary identifier. If `person` is `nil`, this method raises an exception.

Distribution identifiers let you use groups as distribution lists, by indicating which value in a multivalue property should be used when addressing the group. See [`Address Book Programming Guide for Mac`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/AddressBook.html#//apple_ref/doc/uid/10000117i) for more detailed discussion.

## Parameters

- `identifier`: The identifier to be set as the distribution identifier
- `property`: The property whose distribution identifier will be set.
- `person`: The person whose distribution identifier will be.

## See Also

- [func distributionIdentifier(forProperty: String!, person: ABPerson!) -> String!](abgroup/distributionidentifier(forproperty:person:).md)
  Returns the distribution identifier for the given property and person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/setdistributionidentifier(_:forproperty:person:))*