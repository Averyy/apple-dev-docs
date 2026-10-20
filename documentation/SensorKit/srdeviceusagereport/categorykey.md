# SRDeviceUsageReport.CategoryKey

**Framework**: SensorKit  
**Kind**: struct  
**Role**: Structure

Categories of apps or websites that the user uses.

## Declaration

```swift
struct CategoryKey
```

```c
typedef NSString * SRDeviceUsageCategoryKey;
```

## Topics

### Initializers
- [init(rawValue: String)](./categorykey/init%28rawvalue%29.md)
  Creates a new category.
### Categories
- [static let books: SRDeviceUsageReport.CategoryKey](./categorykey/books.md)
  An app category for reading books.
- [static let business: SRDeviceUsageReport.CategoryKey](./categorykey/business.md)
  An app category for doing business.
- [static let catalogs: SRDeviceUsageReport.CategoryKey](./categorykey/catalogs.md)
  An app category for reading catalogs.
- [static let developerTools: SRDeviceUsageReport.CategoryKey](./categorykey/developertools.md)
  An app category for creating apps.
- [static let education: SRDeviceUsageReport.CategoryKey](./categorykey/education.md)
  An app category for learning.
- [static let entertainment: SRDeviceUsageReport.CategoryKey](./categorykey/entertainment.md)
  An app category for entertainment.
- [static let finance: SRDeviceUsageReport.CategoryKey](./categorykey/finance.md)
  An app category for finance.
- [static let foodAndDrink: SRDeviceUsageReport.CategoryKey](./categorykey/foodanddrink.md)
  An app category for dining.
- [static let games: SRDeviceUsageReport.CategoryKey](./categorykey/games.md)
  An app category for gaming.
- [static let graphicsAndDesign: SRDeviceUsageReport.CategoryKey](./categorykey/graphicsanddesign.md)
  An app category for graphic design.
- [static let healthAndFitness: SRDeviceUsageReport.CategoryKey](./categorykey/healthandfitness.md)
  An app category for health and fitness.
- [static let kids: SRDeviceUsageReport.CategoryKey](./categorykey/kids.md)
  An app category for children.
- [static let lifestyle: SRDeviceUsageReport.CategoryKey](./categorykey/lifestyle.md)
  An app category for lifestyle.
- [static let medical: SRDeviceUsageReport.CategoryKey](./categorykey/medical.md)
  An app category for healthcare.
- [static let miscellaneous: SRDeviceUsageReport.CategoryKey](./categorykey/miscellaneous.md)
  An app category for miscellaneous apps.
- [static let music: SRDeviceUsageReport.CategoryKey](./categorykey/music.md)
  An app category for music.
- [static let navigation: SRDeviceUsageReport.CategoryKey](./categorykey/navigation.md)
  An app category for navigation.
- [static let news: SRDeviceUsageReport.CategoryKey](./categorykey/news.md)
  An app category for news.
- [static let newsstand: SRDeviceUsageReport.CategoryKey](./categorykey/newsstand.md)
  An app category for Apple News.
- [static let photoAndVideo: SRDeviceUsageReport.CategoryKey](./categorykey/photoandvideo.md)
  An app category for photography and film.
- [static let productivity: SRDeviceUsageReport.CategoryKey](./categorykey/productivity.md)
  An app category for productivity.
- [static let reference: SRDeviceUsageReport.CategoryKey](./categorykey/reference.md)
  An app category for reference.
- [static let shopping: SRDeviceUsageReport.CategoryKey](./categorykey/shopping.md)
  An app category for shopping.
- [static let socialNetworking: SRDeviceUsageReport.CategoryKey](./categorykey/socialnetworking.md)
  An app category for social networking.
- [static let sports: SRDeviceUsageReport.CategoryKey](./categorykey/sports.md)
  An app category for sports.
- [static let stickers: SRDeviceUsageReport.CategoryKey](./categorykey/stickers.md)
  An app category for stickers.
- [static let travel: SRDeviceUsageReport.CategoryKey](./categorykey/travel.md)
  An app category for travel.
- [static let utilities: SRDeviceUsageReport.CategoryKey](./categorykey/utilities.md)
  An app category for utilities.
- [static let weather: SRDeviceUsageReport.CategoryKey](./categorykey/weather.md)
  An app category for weather.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Analyzing App Use
- [var applicationUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.ApplicationUsage]]](./applicationusagebycategory.md)
  The usage time of apps per category.
- [SRDeviceUsageReport.ApplicationUsage](./applicationusage.md)
  An object that describes the user’s app activity over a period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/categorykey)*