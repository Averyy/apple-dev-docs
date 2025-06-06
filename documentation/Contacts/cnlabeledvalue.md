# CNLabeledValue

**Framework**: Contacts  
**Kind**: class

An immutable object that combines a contact property value with a label that describes that property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CNLabeledValue<ValueType> where ValueType : NSCopying, ValueType : NSSecureCoding
```

#### Overview

Labels describe the context for a property. For example, the label for a phone number indicates whether it corresponds to the user’s home, work, or iPhone number.

`CNLabeledValue` objects are thread-safe, and you can access their properties from any thread of your app.

## Topics

### Creating a labeled value
- [init(label: String?, value: ValueType)](cnlabeledvalue/init(label:value:).md)
  Returns a new labeled value identifier.
### Getting the label and value
- [var label: String?](cnlabeledvalue/label.md)
  The label for a contact property value.
- [var value: ValueType](cnlabeledvalue/value.md)
  A contact property value.
### Setting labels and values
- [func settingLabel(String?) -> Self](cnlabeledvalue/settinglabel(_:).md)
  Returns a labeled value object with an existing value and identifier.
- [func settingLabel(String?, value: ValueType) -> Self](cnlabeledvalue/settinglabel(_:value:).md)
  Returns a labeled value object with the specified label and value with the existing identifier.
- [func settingValue(ValueType) -> Self](cnlabeledvalue/settingvalue(_:).md)
  Returns a new value for an existing label and identifier.
### Localizing the label and value
- [class func localizedString(forLabel: String) -> String](cnlabeledvalue/localizedstring(forlabel:).md)
  Returns a localized string for the specified label.
### Getting the unique identifier
- [var identifier: String](cnlabeledvalue/identifier.md)
  A unique identifier for the labeled value object.
### Getting common labels
- [let CNLabelHome: String](cnlabelhome.md)
  The label for identifying home information.
- [let CNLabelWork: String](cnlabelwork.md)
  The label for identifying work information.
- [let CNLabelSchool: String](cnlabelschool.md)
  The label for the contact’s school.
- [let CNLabelOther: String](cnlabelother.md)
  The label for identifying other information.
- [let CNLabelEmailiCloud: String](cnlabelemailicloud.md)
  The label for identifying the contact’s iCloud email information.
- [let CNLabelURLAddressHomePage: String](cnlabelurladdresshomepage.md)
  The label for identifying URL information.
- [let CNLabelDateAnniversary: String](cnlabeldateanniversary.md)
  The label for identifying the contact’s anniversary date.
### Getting phone number labels
- [let CNLabelPhoneNumberMain: String](cnlabelphonenumbermain.md)
  The label for identifying the contact’s main phone number.
- [let CNLabelPhoneNumberiPhone: String](cnlabelphonenumberiphone.md)
  The label for identifying the contact’s iPhone number.
- [let CNLabelPhoneNumberAppleWatch: String](cnlabelphonenumberapplewatch.md)
  The label for identifying the contact’s Apple Watch phone number.
- [let CNLabelPhoneNumberMobile: String](cnlabelphonenumbermobile.md)
  The label for identifying the contact’s mobile phone number.
- [let CNLabelPhoneNumberPager: String](cnlabelphonenumberpager.md)
  The label for identifying the contact’s pager number.
- [let CNLabelPhoneNumberWorkFax: String](cnlabelphonenumberworkfax.md)
  The label for identifying the contact’s work fax number.
- [let CNLabelPhoneNumberHomeFax: String](cnlabelphonenumberhomefax.md)
  The label for identifying the contact’s home fax number.
- [let CNLabelPhoneNumberOtherFax: String](cnlabelphonenumberotherfax.md)
  The label for identifying another fax number.
### Getting immediate family relationship labels
- [let CNLabelContactRelationBrother: String](cnlabelcontactrelationbrother.md)
  The label for the contact’s brother.
- [let CNLabelContactRelationChild: String](cnlabelcontactrelationchild.md)
  The label for the contact’s child.
- [let CNLabelContactRelationDaughter: String](cnlabelcontactrelationdaughter.md)
  The label for the contact’s daughter.
- [let CNLabelContactRelationElderBrother: String](cnlabelcontactrelationelderbrother.md)
  The label for the contact’s elder brother.
- [let CNLabelContactRelationElderSibling: String](cnlabelcontactrelationeldersibling.md)
  The label for the contact’s elder sibling.
- [let CNLabelContactRelationElderSister: String](cnlabelcontactrelationeldersister.md)
  The label for the contact’s elder sister.
- [let CNLabelContactRelationEldestBrother: String](cnlabelcontactrelationeldestbrother.md)
  The label for the contact’s eldest brother.
- [let CNLabelContactRelationEldestSister: String](cnlabelcontactrelationeldestsister.md)
  The label for the contact’s eldest sister.
- [let CNLabelContactRelationFather: String](cnlabelcontactrelationfather.md)
  The label for the contact’s father.
- [let CNLabelContactRelationFemalePartner: String](cnlabelcontactrelationfemalepartner.md)
  The label for the contact’s female partner.
- [let CNLabelContactRelationHusband: String](cnlabelcontactrelationhusband.md)
  The label for the contact’s husband.
- [let CNLabelContactRelationMalePartner: String](cnlabelcontactrelationmalepartner.md)
  The label for the contact’s male partner.
- [let CNLabelContactRelationMother: String](cnlabelcontactrelationmother.md)
  The label for the contact’s mother.
- [let CNLabelContactRelationParent: String](cnlabelcontactrelationparent.md)
  The label for the contact’s parent.
- [let CNLabelContactRelationPartner: String](cnlabelcontactrelationpartner.md)
  The label for the contact’s partner.
- [let CNLabelContactRelationSibling: String](cnlabelcontactrelationsibling.md)
  The label for the contact’s sibling.
- [let CNLabelContactRelationSister: String](cnlabelcontactrelationsister.md)
  The label for the contact’s sister.
- [let CNLabelContactRelationSon: String](cnlabelcontactrelationson.md)
  The label for the contact’s son.
- [let CNLabelContactRelationSpouse: String](cnlabelcontactrelationspouse.md)
  The label for the contact’s spouse.
- [let CNLabelContactRelationStepbrother: String](cnlabelcontactrelationstepbrother.md)
  The label for the contact’s stepbrother.
- [let CNLabelContactRelationStepchild: String](cnlabelcontactrelationstepchild.md)
  The label for the contact’s stepchild.
- [let CNLabelContactRelationStepdaughter: String](cnlabelcontactrelationstepdaughter.md)
  The label for the contact’s stepdaughter.
- [let CNLabelContactRelationStepfather: String](cnlabelcontactrelationstepfather.md)
  The label for the contact’s stepfather.
- [let CNLabelContactRelationStepmother: String](cnlabelcontactrelationstepmother.md)
  The label for the contact’s stepmother.
- [let CNLabelContactRelationStepparent: String](cnlabelcontactrelationstepparent.md)
  The label for the contact’s stepparent.
- [let CNLabelContactRelationStepsister: String](cnlabelcontactrelationstepsister.md)
  The label for the contact’s stepsister.
- [let CNLabelContactRelationStepson: String](cnlabelcontactrelationstepson.md)
  The label for the contact’s stepson.
- [let CNLabelContactRelationWife: String](cnlabelcontactrelationwife.md)
  The label for the contact’s wife.
- [let CNLabelContactRelationYoungerBrother: String](cnlabelcontactrelationyoungerbrother.md)
  The label for the contact’s younger brother.
- [let CNLabelContactRelationYoungerSibling: String](cnlabelcontactrelationyoungersibling.md)
  The label for the contact’s younger sibling.
- [let CNLabelContactRelationYoungerSister: String](cnlabelcontactrelationyoungersister.md)
  The label for the contact’s younger sister.
- [let CNLabelContactRelationYoungestBrother: String](cnlabelcontactrelationyoungestbrother.md)
  The label for the contact’s youngest brother.
- [let CNLabelContactRelationYoungestSister: String](cnlabelcontactrelationyoungestsister.md)
  The label for the contact’s youngest sister.
### Getting acquaintance relationship labels
- [let CNLabelContactRelationBoyfriend: String](cnlabelcontactrelationboyfriend.md)
  The label for the contact’s boyfriend.
- [let CNLabelContactRelationColleague: String](cnlabelcontactrelationcolleague.md)
  The label for the contact’s colleague.
- [let CNLabelContactRelationFemaleFriend: String](cnlabelcontactrelationfemalefriend.md)
  The label for the contact’s female friend.
- [let CNLabelContactRelationFriend: String](cnlabelcontactrelationfriend.md)
  The label for the contact’s friend.
- [let CNLabelContactRelationGirlfriend: String](cnlabelcontactrelationgirlfriend.md)
  The label for the contact’s girlfriend.
- [let CNLabelContactRelationGirlfriendOrBoyfriend: String](cnlabelcontactrelationgirlfriendorboyfriend.md)
  The label for the contact’s girlfriend or boyfriend.
- [let CNLabelContactRelationMaleFriend: String](cnlabelcontactrelationmalefriend.md)
  The label for the contact’s male friend.
### Getting business relationship labels
- [let CNLabelContactRelationAssistant: String](cnlabelcontactrelationassistant.md)
  The label for the contact’s assistant.
- [let CNLabelContactRelationManager: String](cnlabelcontactrelationmanager.md)
  The label for the contact’s manager.
### Getting education relationship labels
- [let CNLabelContactRelationTeacher: String](cnlabelcontactrelationteacher.md)
  The label for the contact’s teacher.
### Getting in-law relationship labels
- [let CNLabelContactRelationBrotherInLaw: String](cnlabelcontactrelationbrotherinlaw.md)
  The label for the contact’s brother-in-law.
- [let CNLabelContactRelationBrotherInLawElderSistersHusband: String](cnlabelcontactrelationbrotherinlaweldersistershusband.md)
  The label for the contact’s elder sister’s husband.
- [let CNLabelContactRelationBrotherInLawHusbandsBrother: String](cnlabelcontactrelationbrotherinlawhusbandsbrother.md)
  The label for the contact’s husband’s brother.
- [let CNLabelContactRelationBrotherInLawHusbandsSistersHusband: String](cnlabelcontactrelationbrotherinlawhusbandssistershusband.md)
  The label for the contact’s husband’s sister’s husband.
- [let CNLabelContactRelationBrotherInLawSistersHusband: String](cnlabelcontactrelationbrotherinlawsistershusband.md)
  The label for the contact’s sister’s husband.
- [let CNLabelContactRelationBrotherInLawSpousesBrother: String](cnlabelcontactrelationbrotherinlawspousesbrother.md)
  The label for the contact’s spouse’s brother.
- [let CNLabelContactRelationBrotherInLawWifesBrother: String](cnlabelcontactrelationbrotherinlawwifesbrother.md)
  The label for the contact’s wife’s brother.
- [let CNLabelContactRelationBrotherInLawWifesSistersHusband: String](cnlabelcontactrelationbrotherinlawwifessistershusband.md)
  The label for the contact’s wife’s sister’s husband.
- [let CNLabelContactRelationBrotherInLawYoungerSistersHusband: String](cnlabelcontactrelationbrotherinlawyoungersistershusband.md)
  The label for the contact’s younger sister’s husband.
- [let CNLabelContactRelationChildInLaw: String](cnlabelcontactrelationchildinlaw.md)
  The label for the contact’s child-in-law.
- [let CNLabelContactRelationCoBrotherInLaw: String](cnlabelcontactrelationcobrotherinlaw.md)
  The label for the contact’s co-brother-in-law.
- [let CNLabelContactRelationCoFatherInLaw: String](cnlabelcontactrelationcofatherinlaw.md)
  The label for the contact’s co-father-in-law.
- [let CNLabelContactRelationCoMotherInLaw: String](cnlabelcontactrelationcomotherinlaw.md)
  The label for the contact’s co-mother-in-law.
- [let CNLabelContactRelationCoParentInLaw: String](cnlabelcontactrelationcoparentinlaw.md)
  The label for the contact’s co-parent-in-law.
- [let CNLabelContactRelationCoSiblingInLaw: String](cnlabelcontactrelationcosiblinginlaw.md)
  The label for the contact’s co-sibling-in-law.
- [let CNLabelContactRelationCoSisterInLaw: String](cnlabelcontactrelationcosisterinlaw.md)
  The label for the contact’s co-sister-in-law.
- [let CNLabelContactRelationElderBrotherInLaw: String](cnlabelcontactrelationelderbrotherinlaw.md)
  The label for the contact’s elder brother-in-law.
- [let CNLabelContactRelationElderSiblingInLaw: String](cnlabelcontactrelationeldersiblinginlaw.md)
  The label for the contact’s elder sibling-in-law.
- [let CNLabelContactRelationElderSisterInLaw: String](cnlabelcontactrelationeldersisterinlaw.md)
  The label for the contact’s elder sister-in-law.
- [let CNLabelContactRelationFatherInLaw: String](cnlabelcontactrelationfatherinlaw.md)
  The label for the contact’s father-in-law.
- [let CNLabelContactRelationFatherInLawHusbandsFather: String](cnlabelcontactrelationfatherinlawhusbandsfather.md)
  The label for the contact’s husband’s father.
- [let CNLabelContactRelationFatherInLawOrStepfather: String](cnlabelcontactrelationfatherinlaworstepfather.md)
  The label for the contact’s father-in-law or stepfather.
- [let CNLabelContactRelationFatherInLawWifesFather: String](cnlabelcontactrelationfatherinlawwifesfather.md)
  The label for the contact’s wife’s father.
- [let CNLabelContactRelationMotherInLaw: String](cnlabelcontactrelationmotherinlaw.md)
  The label for the contact’s mother-in-law.
- [let CNLabelContactRelationMotherInLawHusbandsMother: String](cnlabelcontactrelationmotherinlawhusbandsmother.md)
  The label for the contact’s husband’s mother.
- [let CNLabelContactRelationMotherInLawOrStepmother: String](cnlabelcontactrelationmotherinlaworstepmother.md)
  The label for the contact’s mother-in-law or stepmother.
- [let CNLabelContactRelationMotherInLawWifesMother: String](cnlabelcontactrelationmotherinlawwifesmother.md)
  The label for the contact’s wife’s mother.
- [let CNLabelContactRelationParentInLaw: String](cnlabelcontactrelationparentinlaw.md)
  The label for the contact’s parent-in-law.
- [let CNLabelContactRelationSiblingInLaw: String](cnlabelcontactrelationsiblinginlaw.md)
  The label for the contact’s sibling-in-law.
- [let CNLabelContactRelationSisterInLaw: String](cnlabelcontactrelationsisterinlaw.md)
  The label for the contact’s sister-in-law.
- [let CNLabelContactRelationSisterInLawBrothersWife: String](cnlabelcontactrelationsisterinlawbrotherswife.md)
  The label for the contact’s brother’s wife.
- [let CNLabelContactRelationSisterInLawElderBrothersWife: String](cnlabelcontactrelationsisterinlawelderbrotherswife.md)
  The label for the contact’s elder brother’s wife.
- [let CNLabelContactRelationSisterInLawHusbandsBrothersWife: String](cnlabelcontactrelationsisterinlawhusbandsbrotherswife.md)
  The label for the contact’s husband’s brother’s wife.
- [let CNLabelContactRelationSisterInLawHusbandsSister: String](cnlabelcontactrelationsisterinlawhusbandssister.md)
  The label for the contact’s husband’s sister.
- [let CNLabelContactRelationSisterInLawSpousesSister: String](cnlabelcontactrelationsisterinlawspousessister.md)
  The label for the contact’s spouse’s sister.
- [let CNLabelContactRelationSisterInLawWifesBrothersWife: String](cnlabelcontactrelationsisterinlawwifesbrotherswife.md)
  The label for the contact’s wife’s brother’s wife.
- [let CNLabelContactRelationSisterInLawWifesSister: String](cnlabelcontactrelationsisterinlawwifessister.md)
  The label for the contact’s wife’s sister.
- [let CNLabelContactRelationSisterInLawYoungerBrothersWife: String](cnlabelcontactrelationsisterinlawyoungerbrotherswife.md)
  The label for the contact’s younger brother’s wife.
- [let CNLabelContactRelationYoungerBrotherInLaw: String](cnlabelcontactrelationyoungerbrotherinlaw.md)
  The label for the contact’s younger brother-in-law.
- [let CNLabelContactRelationYoungerSiblingInLaw: String](cnlabelcontactrelationyoungersiblinginlaw.md)
  The label for the contact’s younger sibling-in-law.
- [let CNLabelContactRelationYoungerSisterInLaw: String](cnlabelcontactrelationyoungersisterinlaw.md)
  The label for the contact’s younger sister-in-law.
### Getting extended family relationship labels
- [let CNLabelContactRelationAunt: String](cnlabelcontactrelationaunt.md)
  The label for the contact’s aunt.
- [let CNLabelContactRelationAuntFathersBrothersWife: String](cnlabelcontactrelationauntfathersbrotherswife.md)
  The label for the contact’s father’s brother’s wife.
- [let CNLabelContactRelationAuntFathersElderBrothersWife: String](cnlabelcontactrelationauntfatherselderbrotherswife.md)
  The label for the contact’s father’s elder brother’s wife.
- [let CNLabelContactRelationAuntFathersElderSister: String](cnlabelcontactrelationauntfatherseldersister.md)
  The label for the contact’s father’s elder sister.
- [let CNLabelContactRelationAuntFathersSister: String](cnlabelcontactrelationauntfatherssister.md)
  The label for the contact’s father’s sister.
- [let CNLabelContactRelationAuntFathersYoungerBrothersWife: String](cnlabelcontactrelationauntfathersyoungerbrotherswife.md)
  The label for the contact’s father’s younger brother’s wife.
- [let CNLabelContactRelationAuntFathersYoungerSister: String](cnlabelcontactrelationauntfathersyoungersister.md)
  The label for the contact’s father’s younger sister.
- [let CNLabelContactRelationAuntMothersBrothersWife: String](cnlabelcontactrelationauntmothersbrotherswife.md)
  The label for the contact’s mother’s brother’s wife.
- [let CNLabelContactRelationAuntMothersElderSister: String](cnlabelcontactrelationauntmotherseldersister.md)
  The label for the contact’s mother’s elder sister.
- [let CNLabelContactRelationAuntMothersSister: String](cnlabelcontactrelationauntmotherssister.md)
  The label for the contact’s mother’s sister.
- [let CNLabelContactRelationAuntMothersYoungerSister: String](cnlabelcontactrelationauntmothersyoungersister.md)
  The label for the contact’s mother’s younger sister.
- [let CNLabelContactRelationAuntParentsElderSister: String](cnlabelcontactrelationauntparentseldersister.md)
  The label for the contact’s parent’s elder sister.
- [let CNLabelContactRelationAuntParentsSister: String](cnlabelcontactrelationauntparentssister.md)
  The label for the contact’s parent’s sister.
- [let CNLabelContactRelationAuntParentsYoungerSister: String](cnlabelcontactrelationauntparentsyoungersister.md)
  The label for the contact’s parent’s younger sister.
- [let CNLabelContactRelationCousin: String](cnlabelcontactrelationcousin.md)
  The label for the contact’s cousin.
- [let CNLabelContactRelationCousinFathersBrothersDaughter: String](cnlabelcontactrelationcousinfathersbrothersdaughter.md)
  The label for the contact’s father’s brother’s daughter.
- [let CNLabelContactRelationCousinFathersBrothersSon: String](cnlabelcontactrelationcousinfathersbrothersson.md)
  The label for the contact’s father’s brother’s son.
- [let CNLabelContactRelationCousinFathersSistersDaughter: String](cnlabelcontactrelationcousinfatherssistersdaughter.md)
  The label for the contact’s father’s sister’s daughter.
- [let CNLabelContactRelationCousinFathersSistersSon: String](cnlabelcontactrelationcousinfatherssistersson.md)
  The label for the contact’s father’s sister’s son.
- [let CNLabelContactRelationCousinGrandparentsSiblingsChild: String](cnlabelcontactrelationcousingrandparentssiblingschild.md)
  The label for the contact’s grandparent’s sibling’s child.
- [let CNLabelContactRelationCousinGrandparentsSiblingsDaughter: String](cnlabelcontactrelationcousingrandparentssiblingsdaughter.md)
  The label for the contact’s grandparent’s sibling’s daughter.
- [let CNLabelContactRelationCousinGrandparentsSiblingsSon: String](cnlabelcontactrelationcousingrandparentssiblingsson.md)
  The label for the contact’s grandparent’s sibling’s son.
- [let CNLabelContactRelationCousinMothersBrothersDaughter: String](cnlabelcontactrelationcousinmothersbrothersdaughter.md)
  The label for the contact’s mother’s brother’s daughter.
- [let CNLabelContactRelationCousinMothersBrothersSon: String](cnlabelcontactrelationcousinmothersbrothersson.md)
  The label for the contact’s mother’s brother’s son.
- [let CNLabelContactRelationCousinMothersSistersDaughter: String](cnlabelcontactrelationcousinmotherssistersdaughter.md)
  The label for the contact’s mother’s sister’s daughter.
- [let CNLabelContactRelationCousinMothersSistersSon: String](cnlabelcontactrelationcousinmotherssistersson.md)
  The label for the contact’s mother’s sister’s son.
- [let CNLabelContactRelationCousinOrSiblingsChild: String](cnlabelcontactrelationcousinorsiblingschild.md)
  The label for the contact’s cousin’s or sibling’s child.
- [let CNLabelContactRelationCousinParentsSiblingsChild: String](cnlabelcontactrelationcousinparentssiblingschild.md)
  The label for the contact’s parent’s sibling’s child.
- [let CNLabelContactRelationCousinParentsSiblingsDaughter: String](cnlabelcontactrelationcousinparentssiblingsdaughter.md)
  The label for the contact’s parent’s sibling’s daughter.
- [let CNLabelContactRelationCousinParentsSiblingsSon: String](cnlabelcontactrelationcousinparentssiblingsson.md)
  The label for the contact’s parent’s sibling’s son.
- [let CNLabelContactRelationDaughterInLaw: String](cnlabelcontactrelationdaughterinlaw.md)
  The label for the contact’s daughter-in-law.
- [let CNLabelContactRelationDaughterInLawOrSisterInLaw: String](cnlabelcontactrelationdaughterinlaworsisterinlaw.md)
  The label for the contact’s daughter-in-law or sister-in-law.
- [let CNLabelContactRelationDaughterInLawOrStepdaughter: String](cnlabelcontactrelationdaughterinlaworstepdaughter.md)
  The label for the contact’s daughter-in-law or stepdaughter.
- [let CNLabelContactRelationElderCousin: String](cnlabelcontactrelationeldercousin.md)
  The label for the contact’s elder cousin.
- [let CNLabelContactRelationElderCousinFathersBrothersDaughter: String](cnlabelcontactrelationeldercousinfathersbrothersdaughter.md)
  The label for the contact’s father’s brother’s daughter.
- [let CNLabelContactRelationElderCousinFathersBrothersSon: String](cnlabelcontactrelationeldercousinfathersbrothersson.md)
  The label for the contact’s father’s brother’s son.
- [let CNLabelContactRelationElderCousinFathersSistersDaughter: String](cnlabelcontactrelationeldercousinfatherssistersdaughter.md)
  The label for the contact’s father’s sister’s daughter.
- [let CNLabelContactRelationElderCousinFathersSistersSon: String](cnlabelcontactrelationeldercousinfatherssistersson.md)
  The label for the contact’s father’s sister’s son.
- [let CNLabelContactRelationElderCousinMothersBrothersDaughter: String](cnlabelcontactrelationeldercousinmothersbrothersdaughter.md)
  The label for the contact’s mother’s brother’s daughter.
- [let CNLabelContactRelationElderCousinMothersBrothersSon: String](cnlabelcontactrelationeldercousinmothersbrothersson.md)
  The label for the contact’s mother’s brother’s son.
- [let CNLabelContactRelationElderCousinMothersSiblingsDaughterOrFathersSistersDaughter: String](cnlabelcontactrelationeldercousinmotherssiblingsdaughterorfatherssistersdaughter.md)
  The label for the contact’s mother’s sibling’s daughter or father’s sister’s daughter.
- [let CNLabelContactRelationElderCousinMothersSiblingsSonOrFathersSistersSon: String](cnlabelcontactrelationeldercousinmotherssiblingssonorfatherssistersson.md)
  The label for the contact’s mother’s sibling’s son or father’s sister’s son.
- [let CNLabelContactRelationElderCousinMothersSistersDaughter: String](cnlabelcontactrelationeldercousinmotherssistersdaughter.md)
  The label for the contact’s mother’s sister’s daughter.
- [let CNLabelContactRelationElderCousinMothersSistersSon: String](cnlabelcontactrelationeldercousinmotherssistersson.md)
  The label for the contact’s mother’s sister’s son.
- [let CNLabelContactRelationElderCousinParentsSiblingsDaughter: String](cnlabelcontactrelationeldercousinparentssiblingsdaughter.md)
  The label for the contact’s parent’s sibling’s daughter.
- [let CNLabelContactRelationElderCousinParentsSiblingsSon: String](cnlabelcontactrelationeldercousinparentssiblingsson.md)
  The label for the contact’s parent’s sibling’s son.
- [let CNLabelContactRelationFemaleCousin: String](cnlabelcontactrelationfemalecousin.md)
  The label for the contact’s female cousin.
- [let CNLabelContactRelationGrandaunt: String](cnlabelcontactrelationgrandaunt.md)
  The label for the contact’s grandaunt.
- [let CNLabelContactRelationGrandchild: String](cnlabelcontactrelationgrandchild.md)
  The label for the contact’s grandchild.
- [let CNLabelContactRelationGrandchildOrSiblingsChild: String](cnlabelcontactrelationgrandchildorsiblingschild.md)
  The label for the contact’s grandchild or sibling’s child.
- [let CNLabelContactRelationGranddaughter: String](cnlabelcontactrelationgranddaughter.md)
  The label for the contact’s granddaughter.
- [let CNLabelContactRelationGranddaughterDaughtersDaughter: String](cnlabelcontactrelationgranddaughterdaughtersdaughter.md)
  The label for the contact’s daughter’s daughter.
- [let CNLabelContactRelationGranddaughterSonsDaughter: String](cnlabelcontactrelationgranddaughtersonsdaughter.md)
  The label for the contact’s son’s daughter.
- [let CNLabelContactRelationGranddaughterOrNiece: String](cnlabelcontactrelationgranddaughterorniece.md)
  The label for the contact’s granddaughter or niece.
- [let CNLabelContactRelationGrandfather: String](cnlabelcontactrelationgrandfather.md)
  The label for the contact’s grandfather.
- [let CNLabelContactRelationGrandfatherFathersFather: String](cnlabelcontactrelationgrandfatherfathersfather.md)
  The label for the contact’s father’s father.
- [let CNLabelContactRelationGrandfatherMothersFather: String](cnlabelcontactrelationgrandfathermothersfather.md)
  The label for the contact’s mother’s father.
- [let CNLabelContactRelationGrandmother: String](cnlabelcontactrelationgrandmother.md)
  The label for the contact’s grandmother.
- [let CNLabelContactRelationGrandmotherFathersMother: String](cnlabelcontactrelationgrandmotherfathersmother.md)
  The label for the contact’s father’s mother.
- [let CNLabelContactRelationGrandmotherMothersMother: String](cnlabelcontactrelationgrandmothermothersmother.md)
  The label for the contact’s mother’s mother.
- [let CNLabelContactRelationGrandnephew: String](cnlabelcontactrelationgrandnephew.md)
  The label for the contact’s grandnephew.
- [let CNLabelContactRelationGrandnephewBrothersGrandson: String](cnlabelcontactrelationgrandnephewbrothersgrandson.md)
  The label for the contact’s brother’s grandson.
- [let CNLabelContactRelationGrandnephewSistersGrandson: String](cnlabelcontactrelationgrandnephewsistersgrandson.md)
  The label for the contact’s sister’s grandson.
- [let CNLabelContactRelationGrandniece: String](cnlabelcontactrelationgrandniece.md)
  The label for the contact’s grandniece.
- [let CNLabelContactRelationGrandnieceBrothersGranddaughter: String](cnlabelcontactrelationgrandniecebrothersgranddaughter.md)
  The label for the contact’s brother’s granddaughter.
- [let CNLabelContactRelationGrandnieceSistersGranddaughter: String](cnlabelcontactrelationgrandniecesistersgranddaughter.md)
  The label for the contact’s sister’s granddaughter.
- [let CNLabelContactRelationGrandparent: String](cnlabelcontactrelationgrandparent.md)
  The label for the contact’s grandparent.
- [let CNLabelContactRelationGrandson: String](cnlabelcontactrelationgrandson.md)
  The label for the contact’s grandson.
- [let CNLabelContactRelationGrandsonDaughtersSon: String](cnlabelcontactrelationgrandsondaughtersson.md)
  The label for the contact’s daughter’s son.
- [let CNLabelContactRelationGrandsonSonsSon: String](cnlabelcontactrelationgrandsonsonsson.md)
  The label for the contact’s son’s son.
- [let CNLabelContactRelationGrandsonOrNephew: String](cnlabelcontactrelationgrandsonornephew.md)
  The label for the contact’s grandson or nephew.
- [let CNLabelContactRelationGranduncle: String](cnlabelcontactrelationgranduncle.md)
  The label for the contact’s granduncle.
- [let CNLabelContactRelationGreatGrandchild: String](cnlabelcontactrelationgreatgrandchild.md)
  The label for the contact’s grandchild.
- [let CNLabelContactRelationGreatGrandchildOrSiblingsGrandchild: String](cnlabelcontactrelationgreatgrandchildorsiblingsgrandchild.md)
  The label for the contact’s grandchild or sibling’s grandchild.
- [let CNLabelContactRelationGreatGranddaughter: String](cnlabelcontactrelationgreatgranddaughter.md)
  The label for the contact’s great-granddaughter.
- [let CNLabelContactRelationGreatGrandfather: String](cnlabelcontactrelationgreatgrandfather.md)
  The label for the contact’s great-grandfather.
- [let CNLabelContactRelationGreatGrandmother: String](cnlabelcontactrelationgreatgrandmother.md)
  The label for the contact’s great-grandmother.
- [let CNLabelContactRelationGreatGrandparent: String](cnlabelcontactrelationgreatgrandparent.md)
  The label for the contact’s great-grandparent.
- [let CNLabelContactRelationGreatGrandson: String](cnlabelcontactrelationgreatgrandson.md)
  The label for the contact’s great-grandson.
- [let CNLabelContactRelationMaleCousin: String](cnlabelcontactrelationmalecousin.md)
  The label for the contact’s male cousin.
- [let CNLabelContactRelationNephew: String](cnlabelcontactrelationnephew.md)
  The label for the contact’s nephew.
- [let CNLabelContactRelationNephewBrothersSon: String](cnlabelcontactrelationnephewbrothersson.md)
  The label for the contact’s brother’s son.
- [let CNLabelContactRelationNephewBrothersSonOrHusbandsSiblingsSon: String](cnlabelcontactrelationnephewbrotherssonorhusbandssiblingsson.md)
  The label for the contact’s brother’s son or husband’s sibling’s son.
- [let CNLabelContactRelationNephewOrCousin: String](cnlabelcontactrelationnepheworcousin.md)
  The label for the contact’s nephew or cousin.
- [let CNLabelContactRelationNephewSistersSon: String](cnlabelcontactrelationnephewsistersson.md)
  The label for the contact’s sister’s son.
- [let CNLabelContactRelationNephewSistersSonOrWifesSiblingsSon: String](cnlabelcontactrelationnephewsisterssonorwifessiblingsson.md)
  The label for the contact’s sister’s son or wife’s sibling’s son.
- [let CNLabelContactRelationNiece: String](cnlabelcontactrelationniece.md)
  The label for the contact’s niece.
- [let CNLabelContactRelationNieceBrothersDaughter: String](cnlabelcontactrelationniecebrothersdaughter.md)
  The label for the contact’s brother’s daughter.
- [let CNLabelContactRelationNieceBrothersDaughterOrHusbandsSiblingsDaughter: String](cnlabelcontactrelationniecebrothersdaughterorhusbandssiblingsdaughter.md)
  The label for the contact’s brother’s daughter or husband’s sibling’s daughter.
- [let CNLabelContactRelationNieceOrCousin: String](cnlabelcontactrelationnieceorcousin.md)
  The label for the contact’s niece or cousin.
- [let CNLabelContactRelationNieceSistersDaughter: String](cnlabelcontactrelationniecesistersdaughter.md)
  The label for the contact’s sister’s daughter.
- [let CNLabelContactRelationNieceSistersDaughterOrWifesSiblingsDaughter: String](cnlabelcontactrelationniecesistersdaughterorwifessiblingsdaughter.md)
  The label for the contact’s sister’s daughter or wife’s sibling’s daughter.
- [let CNLabelContactRelationParentsElderSibling: String](cnlabelcontactrelationparentseldersibling.md)
  The label for the contact’s parent’s elder sibling.
- [let CNLabelContactRelationParentsSibling: String](cnlabelcontactrelationparentssibling.md)
  The label for the contact’s parent’s sibling.
- [let CNLabelContactRelationParentsSiblingFathersElderSibling: String](cnlabelcontactrelationparentssiblingfatherseldersibling.md)
  The label for the contact’s father’s elder sibling.
- [let CNLabelContactRelationParentsSiblingFathersSibling: String](cnlabelcontactrelationparentssiblingfatherssibling.md)
  The label for the contact’s father’s sibling.
- [let CNLabelContactRelationParentsSiblingFathersYoungerSibling: String](cnlabelcontactrelationparentssiblingfathersyoungersibling.md)
  The label for the contact’s father’s youngest sibling.
- [let CNLabelContactRelationParentsSiblingMothersElderSibling: String](cnlabelcontactrelationparentssiblingmotherseldersibling.md)
  The label for the contact’s mother’s elder sibling.
- [let CNLabelContactRelationParentsSiblingMothersSibling: String](cnlabelcontactrelationparentssiblingmotherssibling.md)
  The label for the contact’s mother’s sibling.
- [let CNLabelContactRelationParentsSiblingMothersYoungerSibling: String](cnlabelcontactrelationparentssiblingmothersyoungersibling.md)
  The label for the contact’s mother’s younger sibling.
- [let CNLabelContactRelationParentsYoungerSibling: String](cnlabelcontactrelationparentsyoungersibling.md)
  The label for the contact’s parent’s younger sibling.
- [let CNLabelContactRelationSiblingsChild: String](cnlabelcontactrelationsiblingschild.md)
  The label for the contact’s sibling’s child.
- [let CNLabelContactRelationSonInLaw: String](cnlabelcontactrelationsoninlaw.md)
  The label for the contact’s son-in-law.
- [let CNLabelContactRelationSonInLawOrBrotherInLaw: String](cnlabelcontactrelationsoninlaworbrotherinlaw.md)
  The label for the contact’s son-in-law or brother-in-law.
- [let CNLabelContactRelationSonInLawOrStepson: String](cnlabelcontactrelationsoninlaworstepson.md)
  The label for the contact’s son-in-law or stepson.
- [let CNLabelContactRelationUncle: String](cnlabelcontactrelationuncle.md)
  The label for the contact’s uncle.
- [let CNLabelContactRelationUncleFathersBrother: String](cnlabelcontactrelationunclefathersbrother.md)
  The label for the contact’s father’s brother.
- [let CNLabelContactRelationUncleFathersElderBrother: String](cnlabelcontactrelationunclefatherselderbrother.md)
  The label for the contact’s father’s elder brother.
- [let CNLabelContactRelationUncleFathersElderSistersHusband: String](cnlabelcontactrelationunclefatherseldersistershusband.md)
  The label for the contact’s elder sister’s husband.
- [let CNLabelContactRelationUncleFathersSistersHusband: String](cnlabelcontactrelationunclefatherssistershusband.md)
  The label for the contact’s father’s sister’s husband.
- [let CNLabelContactRelationUncleFathersYoungerBrother: String](cnlabelcontactrelationunclefathersyoungerbrother.md)
  The label for the contact’s father’s younger brother.
- [let CNLabelContactRelationUncleFathersYoungerSistersHusband: String](cnlabelcontactrelationunclefathersyoungersistershusband.md)
  The label for the contact’s father’s younger sister’s husband.
- [let CNLabelContactRelationUncleMothersBrother: String](cnlabelcontactrelationunclemothersbrother.md)
  The label for the contact’s mother’s brother.
- [let CNLabelContactRelationUncleMothersElderBrother: String](cnlabelcontactrelationunclemotherselderbrother.md)
  The label for the contact’s mother’s elder brother.
- [let CNLabelContactRelationUncleMothersSistersHusband: String](cnlabelcontactrelationunclemotherssistershusband.md)
  The label for the contact’s mother’s sister’s husband.
- [let CNLabelContactRelationUncleMothersYoungerBrother: String](cnlabelcontactrelationunclemothersyoungerbrother.md)
  The label for the contact’s mother’s younger brother.
- [let CNLabelContactRelationUncleParentsBrother: String](cnlabelcontactrelationuncleparentsbrother.md)
  The label for the contact’s parent’s brother.
- [let CNLabelContactRelationUncleParentsElderBrother: String](cnlabelcontactrelationuncleparentselderbrother.md)
  The label for the contact’s parent’s elder brother.
- [let CNLabelContactRelationUncleParentsYoungerBrother: String](cnlabelcontactrelationuncleparentsyoungerbrother.md)
  The label for the contact’s parent’s younger brother.
- [let CNLabelContactRelationYoungerCousin: String](cnlabelcontactrelationyoungercousin.md)
  The label for the contact’s younger cousin.
- [let CNLabelContactRelationYoungerCousinFathersBrothersDaughter: String](cnlabelcontactrelationyoungercousinfathersbrothersdaughter.md)
  The label for the contact’s father’s brother’s younger daughter.
- [let CNLabelContactRelationYoungerCousinFathersBrothersSon: String](cnlabelcontactrelationyoungercousinfathersbrothersson.md)
  The label for the contact’s father’s brother’s younger son.
- [let CNLabelContactRelationYoungerCousinFathersSistersDaughter: String](cnlabelcontactrelationyoungercousinfatherssistersdaughter.md)
  The label for the contact’s father’s sister’s younger daughter.
- [let CNLabelContactRelationYoungerCousinFathersSistersSon: String](cnlabelcontactrelationyoungercousinfatherssistersson.md)
  The label for the contact’s father’s sister’s younger son.
- [let CNLabelContactRelationYoungerCousinMothersBrothersDaughter: String](cnlabelcontactrelationyoungercousinmothersbrothersdaughter.md)
  The label for the contact’s mother’s brother’s younger daughter.
- [let CNLabelContactRelationYoungerCousinMothersBrothersSon: String](cnlabelcontactrelationyoungercousinmothersbrothersson.md)
  The label for the contact’s mother’s brother’s younger son.
- [let CNLabelContactRelationYoungerCousinMothersSiblingsDaughterOrFathersSistersDaughter: String](cnlabelcontactrelationyoungercousinmotherssiblingsdaughterorfatherssistersdaughter.md)
  The label for the contact’s mother’s sibling’s younger daughter or father’s sister’s younger daughter.
- [let CNLabelContactRelationYoungerCousinMothersSiblingsSonOrFathersSistersSon: String](cnlabelcontactrelationyoungercousinmotherssiblingssonorfatherssistersson.md)
  The label for the contact’s mother’s sibling’s younger son or father’s sister’s younger son.
- [let CNLabelContactRelationYoungerCousinMothersSistersDaughter: String](cnlabelcontactrelationyoungercousinmotherssistersdaughter.md)
  The label for the contact’s mother’s sister’s younger daughter.
- [let CNLabelContactRelationYoungerCousinMothersSistersSon: String](cnlabelcontactrelationyoungercousinmotherssistersson.md)
  The label for the contact’s mother’s sister’s younger son.
- [let CNLabelContactRelationYoungerCousinParentsSiblingsDaughter: String](cnlabelcontactrelationyoungercousinparentssiblingsdaughter.md)
  The label for the contact’s parent’s sibling’s younger daughter.
- [let CNLabelContactRelationYoungerCousinParentsSiblingsSon: String](cnlabelcontactrelationyoungercousinparentssiblingsson.md)
  The label for the contact’s parent’s sibling’s younger son.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CNContactProperty](cncontactproperty.md)
  An object that represents a property of a contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnlabeledvalue)*