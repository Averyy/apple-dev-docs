# distributionIdentifier(forProperty:person:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Returns the distribution identifier for the given property and person.

**Availability**:
- macOS

## Declaration

```swift
func distributionIdentifier(forProperty property: String!, person: ABPerson!) -> String!
```

```objc
- (NSString *) distributionIdentifierForProperty:(NSString *) property person:(ABPerson *) person;
```

## Return Value

The distribution identifier for the given property and person.

## Discussion

If a distribution identifier is not set, this method returns the multivalue’s primary identifier. If either the `property` or the `person` argument is `nil`, this method returns `nil`. This method also returns `nil` if `property` is not a multivalue list property, or if `person` is not a member of the group.

Distribution identifiers let you use groups as distribution lists, by indicating which value in a multivalue property should be used when addressing the group. See [Using Address Book Groups as Distribution Lists](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/Tasks/CreatingMailingLists.html#//apple_ref/doc/uid/20001025) for more detailed discussion.

## Parameters

- `property`: The property whose distribution identifier will be returned.
- `person`: The person whose distribution identifier will be returned.

## See Also

### Managing Distribution Lists
- [func setDistributionIdentifier(String!, forProperty: String!, person: ABPerson!) -> Bool](./setdistributionidentifier%28_,forproperty,person%29.md)
  Assigns a specific distribution identifier for a person’s multivalue list property so that the group can be used as a distribution list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/distributionidentifier(forproperty:person:))*