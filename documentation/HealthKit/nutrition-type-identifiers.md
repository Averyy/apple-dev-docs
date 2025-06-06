# Nutrition Type Identifiers

**Framework**: Healthkit

Type identifiers used for tracking diet and nutrition.

#### Overview

Nutritional data can be broadly categorized into two main groups:

- Macronutrients consumed in large quantities, such as fats, carbohydrates, and proteins.
- Micronutrients consumed in smaller quantities, such as vitamins and minerals.

HealthKit also provides type identifiers for nutrition-related items that users may want to track, like water or caffeine.

You do not need to track all nutritional information; you can focus on the items of interest to your users. In general, the data from nutrition labels is a good place to start. Many countries and regions require a nutrition label on packaged food. While the contents of these labels vary from one country or region to another, they typically include the nutritional data represented by these properties:

- [`dietaryEnergyConsumed`](hkquantitytypeidentifier/dietaryenergyconsumed.md)
- [`dietaryFatTotal`](hkquantitytypeidentifier/dietaryfattotal.md)
- [`dietaryFatSaturated`](hkquantitytypeidentifier/dietaryfatsaturated.md)
- [`dietaryCholesterol`](hkquantitytypeidentifier/dietarycholesterol.md)
- [`dietaryCarbohydrates`](hkquantitytypeidentifier/dietarycarbohydrates.md)
- [`dietaryFiber`](hkquantitytypeidentifier/dietaryfiber.md)
- [`dietarySugar`](hkquantitytypeidentifier/dietarysugar.md)
- [`dietaryProtein`](hkquantitytypeidentifier/dietaryprotein.md)
- [`dietaryCalcium`](hkquantitytypeidentifier/dietarycalcium.md)
- [`dietaryIron`](hkquantitytypeidentifier/dietaryiron.md)
- [`dietaryPotassium`](hkquantitytypeidentifier/dietarypotassium.md)
- [`dietarySodium`](hkquantitytypeidentifier/dietarysodium.md)
- [`dietaryVitaminA`](hkquantitytypeidentifier/dietaryvitamina.md)
- [`dietaryVitaminC`](hkquantitytypeidentifier/dietaryvitaminc.md)
- [`dietaryVitaminD`](hkquantitytypeidentifier/dietaryvitamind.md)

##### Combine Nutritional Samples

Macronutrient identifiers can be thought of as a hierarchy. The [`dietaryEnergyConsumed`](hkquantitytypeidentifier/dietaryenergyconsumed.md) identifier represents the total amount of energy from all fats, carbohydrates, and protein. You can provide a detailed breakdown using the [`dietaryFatTotal`](hkquantitytypeidentifier/dietaryfattotal.md), [`dietaryCarbohydrates`](hkquantitytypeidentifier/dietarycarbohydrates.md), and [`dietaryProtein`](hkquantitytypeidentifier/dietaryprotein.md) identifiers. Fats can be further separated into [`dietaryFatMonounsaturated`](hkquantitytypeidentifier/dietaryfatmonounsaturated.md), [`dietaryFatPolyunsaturated`](hkquantitytypeidentifier/dietaryfatpolyunsaturated.md), and [`dietaryFatSaturated`](hkquantitytypeidentifier/dietaryfatsaturated.md). Carbohydrates can be identified as [`dietaryFiber`](hkquantitytypeidentifier/dietaryfiber.md) and [`dietarySugar`](hkquantitytypeidentifier/dietarysugar.md).

Unless your app is very focused (for example, tracking only sugar or saturated fat), always provide the total data ([`dietaryFatTotal`](hkquantitytypeidentifier/dietaryfattotal.md) or [`dietaryCarbohydrates`](hkquantitytypeidentifier/dietarycarbohydrates.md)), and then optionally provide the more detailed information using the subcategories. You do not need to provide data for all of the subcategories; however, the sum of the subcategory sample values should be equal or less than the total sample’s value.

> **Note**:  The [`dietaryEnergyConsumed`](hkquantitytypeidentifier/dietaryenergyconsumed.md) samples are handled differently than the other macronutrients. While it can be seen as a total value,  [`dietaryEnergyConsumed`](hkquantitytypeidentifier/dietaryenergyconsumed.md) is measured in calories or kilojoules, while the individual macronutrient samples are measured by mass.

## Topics

### Essentials
- [static let food: HKCorrelationTypeIdentifier](hkcorrelationtypeidentifier/food.md)
  Food correlation types combine any number of nutritional samples into a single food object.
- [let HKMetadataKeyFoodType: String](hkmetadatakeyfoodtype.md)
  The type of food that the HealthKit object represents.
### Macronutrients
- [static let dietaryEnergyConsumed: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryenergyconsumed.md)
  A quantity sample type that measures the amount of energy consumed.
- [static let dietaryCarbohydrates: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarycarbohydrates.md)
  A quantity sample type that measures the amount of carbohydrates consumed.
- [static let dietaryFiber: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryfiber.md)
  A quantity sample type that measures the amount of fiber consumed.
- [static let dietarySugar: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarysugar.md)
  A quantity sample type that measures the amount of sugar consumed.
- [static let dietaryFatTotal: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryfattotal.md)
  A quantity sample type that measures the total amount of fat consumed.
- [static let dietaryFatMonounsaturated: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryfatmonounsaturated.md)
  A quantity sample type that measures the amount of monounsaturated fat consumed.
- [static let dietaryFatPolyunsaturated: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryfatpolyunsaturated.md)
  A quantity sample type that measures the amount of polyunsaturated fat consumed.
- [static let dietaryFatSaturated: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryfatsaturated.md)
  A quantity sample type that measures the amount of saturated fat consumed.
- [static let dietaryCholesterol: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarycholesterol.md)
  A quantity sample type that measures the amount of cholesterol consumed.
- [static let dietaryProtein: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryprotein.md)
  A quantity sample type that measures the amount of protein consumed.
### Vitamins
- [static let dietaryVitaminA: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryvitamina.md)
  A quantity sample type that measures the amount of vitamin A consumed.
- [static let dietaryThiamin: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarythiamin.md)
  A quantity sample type that measures the amount of thiamin (vitamin B1) consumed.
- [static let dietaryRiboflavin: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryriboflavin.md)
  A quantity sample type that measures the amount of riboflavin (vitamin B2) consumed.
- [static let dietaryNiacin: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryniacin.md)
  A quantity sample type that measures the amount of niacin (vitamin B3) consumed.
- [static let dietaryPantothenicAcid: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarypantothenicacid.md)
  A quantity sample type that measures the amount of pantothenic acid (vitamin B5) consumed.
- [static let dietaryVitaminB6: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryvitaminb6.md)
  A quantity sample type that measures the amount of pyridoxine (vitamin B6) consumed.
- [static let dietaryBiotin: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarybiotin.md)
  A quantity sample type that measures the amount of biotin (vitamin B7) consumed.
- [static let dietaryVitaminB12: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryvitaminb12.md)
  A quantity sample type that measures the amount of cyanocobalamin (vitamin B12) consumed.
- [static let dietaryVitaminC: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryvitaminc.md)
  A quantity sample type that measures the amount of vitamin C consumed.
- [static let dietaryVitaminD: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryvitamind.md)
  A quantity sample type that measures the amount of vitamin D consumed.
- [static let dietaryVitaminE: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryvitamine.md)
  A quantity sample type that measures the amount of vitamin E consumed.
- [static let dietaryVitaminK: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryvitamink.md)
  A quantity sample type that measures the amount of vitamin K consumed.
- [static let dietaryFolate: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryfolate.md)
  A quantity sample type that measures the amount of folate (folic acid) consumed.
### Minerals
- [static let dietaryCalcium: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarycalcium.md)
  A quantity sample type that measures the amount of calcium consumed.
- [static let dietaryChloride: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarychloride.md)
  A quantity sample type that measures the amount of chloride consumed.
- [static let dietaryIron: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryiron.md)
  A quantity sample type that measures the amount of iron consumed.
- [static let dietaryMagnesium: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarymagnesium.md)
  A quantity sample type that measures the amount of magnesium consumed.
- [static let dietaryPhosphorus: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryphosphorus.md)
  A quantity sample type that measures the amount of phosphorus consumed.
- [static let dietaryPotassium: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarypotassium.md)
  A quantity sample type that measures the amount of potassium consumed.
- [static let dietarySodium: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarysodium.md)
  A quantity sample type that measures the amount of sodium consumed.
- [static let dietaryZinc: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryzinc.md)
  A quantity sample type that measures the amount of zinc consumed.
### Hydration
- [static let dietaryWater: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarywater.md)
  A quantity sample type that measures the amount of water consumed.
### Caffeination
- [static let dietaryCaffeine: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarycaffeine.md)
  A quantity sample type that measures the amount of caffeine consumed.
### Ultratrace Minerals
- [static let dietaryChromium: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarychromium.md)
  A quantity sample type that measures the amount of chromium consumed.
- [static let dietaryCopper: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarycopper.md)
  A quantity sample type that measures the amount of copper consumed.
- [static let dietaryIodine: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryiodine.md)
  A quantity sample type that measures the amount of iodine consumed.
- [static let dietaryManganese: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarymanganese.md)
  A quantity sample type that measures the amount of manganese consumed.
- [static let dietaryMolybdenum: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarymolybdenum.md)
  A quantity sample type that measures the amount of molybdenum consumed.
- [static let dietarySelenium: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryselenium.md)
  A quantity sample type that measures the amount of selenium consumed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/HealthKit/nutrition-type-identifiers)*