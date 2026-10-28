# AppClipAdvancedExperienceCreateRequest.Data.Attributes.Place

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The place information of an advanced App Clip experience you create with this request.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```
object AppClipAdvancedExperienceCreateRequest.Data.Attributes.Place
```

## Discussion

Apple Maps uses any location data that you provide solely for matching an App Clip experience to an existing location. If it can’t find a match, Apple Maps doesn’t use the provided location data.

## Topics

### Objects
- [object AppClipAdvancedExperienceCreateRequest.Data.Attributes.Place.DisplayPoint](./place-data.dictionary/displaypoint-data.dictionary.md)
  A point-based representation of a place in Apple Maps.
- [object AppClipAdvancedExperienceCreateRequest.Data.Attributes.Place.MainAddress](./place-data.dictionary/mainaddress-data.dictionary.md)
  The main address for a point of interest or business in Apple Maps.
- [object AppClipAdvancedExperienceCreateRequest.Data.Attributes.Place.PhoneNumber](./place-data.dictionary/phonenumber-data.dictionary.md)
  The phone number of a point of interest or business in Apple Maps.

## Properties

- `categories` ([string]): A list of categories for a place in Apple Maps you associate with the Advanced App Clip experience.
- `displayPoint` (AppClipAdvancedExperienceCreateRequest.Data.Attributes.Place.DisplayPoint): Coordinates of a place in Apple Maps you associate with an advanced App Clip experience.
- `homePage` (string): The optional website URL for a place.
- `mainAddress` (AppClipAdvancedExperienceCreateRequest.Data.Attributes.Place.MainAddress): The main address of a place in Apple Maps. This value is required if you don’t provide coordinates for a place.
- `mapAction` (string): A string that describes the intent behind an App Clip invocation from location-based suggestions from Siri Suggestions and the Maps app.

  **Allowed Values**: `BUY_TICKETS`, `VIEW_AVAILABILITY`, `VIEW_PRICING`, `HOTEL_BOOK_ROOM`, `PARKING_RESERVE_PARKING`, `RESTAURANT_JOIN_WAITLIST`, `RESTAURANT_ORDER_DELIVERY`, `RESTAURANT_ORDER_FOOD`, `RESTAURANT_ORDER_TAKEOUT`, `RESTAURANT_RESERVATION`, `SCHEDULE_APPOINTMENT`, `RESTAURANT_VIEW_MENU`, `THEATER_NOW_PLAYING`, `AIRLINE_BOOK_TRAVEL`, `AIRLINE_CHECK_IN`, `AIRLINE_FLIGHT_STATUS`, `APPLY`, `BOOK`, `BOOK_ACTIVITIES`, `BOOK_RIDES`, `BOOK_TEETIMES`, `BOOK_TOURS`, `CAREERS`, `CHARGE_EV`, `COUPONS`, `DONATE`, `EVENTS`, `EVENTS_SHOWS`, `EVENTS_SPORTS`, `GIFT_CARD`, `HOTEL_AMENITIES`, `JOIN`, `PARKING_AVAILABLE`, `RESTAURANT_PICKUP`, `RETAIL_SERVICE_QUOTE`, `RETAIL_STORE_DELIVERY`, `RETAIL_STORE_PICKUP`, `RETAIL_STORE_SHOP`, `SERVICES`, `SUPPORT`, `PAY_TO_PARK`
- `names` ([string]): An array of names as strings for a place in Apple Maps.
- `phoneNumber` (AppClipAdvancedExperienceCreateRequest.Data.Attributes.Place.PhoneNumber): The phone number that’s associated with a place in Apple Maps as a string.
- `placeId` (string): An opaque ID that uniquely identifies a place. If you previously created a place in Apple Maps for the place you associate with your advanced App Clip experience, use its ID instead of creating a new ID.
- `relationship` (string): A navigational link to related data and included resource types and IDs.

  **Allowed Values**: `OWNER`, `AUTHORIZED`, `OTHER`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipadvancedexperiencecreaterequest/data-data.dictionary/attributes-data.dictionary/place-data.dictionary)*