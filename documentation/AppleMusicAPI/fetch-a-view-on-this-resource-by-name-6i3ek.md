# Get a Catalog Playlist’s Relationship View Directly by Name

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch related resources for a single playlist’s relationship view.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/playlists/pl.cb4d1c09a2df4230a78d0395fe1f8fde/view/featured-artists
```

**Response**:

```json
{
  "next": "/v1/catalog/us/playlists/pl.cb4d1c09a2df4230a78d0395fe1f8fde/view/featured-artists?offset=10",
  "data": [
    {
      "id": "342515428",
      "type": "artists",
      "href": "/v1/catalog/us/artists/342515428",
      "attributes": {
        "genreNames": [
          "Classical Crossover"
        ],
        "url": "https://music.apple.com/us/artist/alexis-ffrench/342515428",
        "name": "Alexis Ffrench",
        "artwork": {
          "width": 4724,
          "height": 4724,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/69/3d/22/693d2250-0258-4866-df47-38a22bb36f37/pr_source.png/{w}x{h}bb.jpg",
          "bgColor": "291c16",
          "textColor1": "e69e6f",
          "textColor2": "db956e",
          "textColor3": "c0845d",
          "textColor4": "b77d5d"
        }
      },
      "relationships": {
        "albums": {
          "href": "/v1/catalog/us/artists/342515428/albums",
          "next": "/v1/catalog/us/artists/342515428/albums?offset=25",
          "data": [
            {
              "id": "1394076344",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1394076344"
            },
            {
              "id": "1482659546",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1482659546"
            },
            {
              "id": "1604808497",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1604808497"
            },
            {
              "id": "1165107327",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1165107327"
            },
            {
              "id": "1034575006",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1034575006"
            },
            {
              "id": "342515423",
              "type": "albums",
              "href": "/v1/catalog/us/albums/342515423"
            },
            {
              "id": "699537799",
              "type": "albums",
              "href": "/v1/catalog/us/albums/699537799"
            },
            {
              "id": "559587594",
              "type": "albums",
              "href": "/v1/catalog/us/albums/559587594"
            },
            {
              "id": "1530215063",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1530215063"
            },
            {
              "id": "1443950844",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1443950844"
            },
            {
              "id": "1508182008",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1508182008"
            },
            {
              "id": "1508182008",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1508182008"
            },
            {
              "id": "1508182008",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1508182008"
            },
            {
              "id": "343188835",
              "type": "albums",
              "href": "/v1/catalog/us/albums/343188835"
            },
            {
              "id": "1538467548",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1538467548"
            },
            {
              "id": "1170901187",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1170901187"
            },
            {
              "id": "1554228517",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1554228517"
            },
            {
              "id": "1450843850",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1450843850"
            },
            {
              "id": "1510968743",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1510968743"
            },
            {
              "id": "1510968743",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1510968743"
            },
            {
              "id": "1448966615",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1448966615"
            },
            {
              "id": "1508176081",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1508176081"
            },
            {
              "id": "1508176081",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1508176081"
            },
            {
              "id": "1506251072",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1506251072"
            },
            {
              "id": "1506251072",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1506251072"
            }
          ]
        }
      }
    },
    {
      "id": "595797008",
      "type": "artists",
      "href": "/v1/catalog/us/artists/595797008",
      "attributes": {
        "genreNames": [
          "Classical"
        ],
        "url": "https://music.apple.com/us/artist/dirk-maassen/595797008",
        "name": "Dirk Maassen",
        "artwork": {
          "width": 3664,
          "height": 3664,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Features125/v4/97/34/b8/9734b8e8-ea27-cc96-5af8-63d81ace6bb0/pr_source.png/{w}x{h}bb.jpg",
          "bgColor": "abb5bf",
          "textColor1": "0c0d0d",
          "textColor2": "0f1112",
          "textColor3": "2b2f31",
          "textColor4": "2e3235"
        }
      },
      "relationships": {
        "albums": {
          "href": "/v1/catalog/us/artists/595797008/albums",
          "next": "/v1/catalog/us/artists/595797008/albums?offset=25",
          "data": [
            {
              "id": "1478320108",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1478320108"
            },
            {
              "id": "1542568083",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1542568083"
            },
            {
              "id": "1375631493",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1375631493"
            },
            {
              "id": "827995329",
              "type": "albums",
              "href": "/v1/catalog/us/albums/827995329"
            },
            {
              "id": "1346631500",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1346631500"
            },
            {
              "id": "1508182008",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1508182008"
            },
            {
              "id": "1508182008",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1508182008"
            },
            {
              "id": "1508182008",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1508182008"
            },
            {
              "id": "1574554097",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1574554097"
            },
            {
              "id": "1604182836",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1604182836"
            },
            {
              "id": "651100556",
              "type": "albums",
              "href": "/v1/catalog/us/albums/651100556"
            },
            {
              "id": "1527770476",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1527770476"
            },
            {
              "id": "960792382",
              "type": "albums",
              "href": "/v1/catalog/us/albums/960792382"
            },
            {
              "id": "1510968710",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1510968710"
            },
            {
              "id": "1064157261",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1064157261"
            },
            {
              "id": "602548192",
              "type": "albums",
              "href": "/v1/catalog/us/albums/602548192"
            },
            {
              "id": "1506251072",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1506251072"
            },
            {
              "id": "1506251072",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1506251072"
            },
            {
              "id": "1509064803",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1509064803"
            },
            {
              "id": "1509064803",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1509064803"
            },
            {
              "id": "1487987937",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1487987937"
            },
            {
              "id": "1487987937",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1487987937"
            },
            {
              "id": "1487987937",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1487987937"
            },
            {
              "id": "1372926551",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1372926551"
            },
            {
              "id": "934606669",
              "type": "albums",
              "href": "/v1/catalog/us/albums/934606669"
            }
          ]
        }
      }
    },
    {
      "id": "1548992806",
      "type": "artists",
      "href": "/v1/catalog/us/artists/1548992806",
      "attributes": {
        "genreNames": [
          "Classical Crossover"
        ],
        "url": "https://music.apple.com/us/artist/wide-eyed/1548992806",
        "name": "Wide Eyed",
        "artwork": {
          "width": 4000,
          "height": 4000,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/3a/01/cc/3a01ccb8-8224-e1d2-5305-273d04162c55/pr_source.png/{w}x{h}bb.jpg",
          "bgColor": "57b4db",
          "textColor1": "100d0b",
          "textColor2": "161211",
          "textColor3": "1e2f34",
          "textColor4": "233239"
        }
      },
      "relationships": {
        "albums": {
          "href": "/v1/catalog/us/artists/1548992806/albums",
          "data": [
            {
              "id": "1608855239",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1608855239"
            },
            {
              "id": "1545908716",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1545908716"
            },
            {
              "id": "1563679230",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1563679230"
            },
            {
              "id": "1607298541",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1607298541"
            },
            {
              "id": "1543377230",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1543377230"
            },
            {
              "id": "1609345197",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1609345197"
            },
            {
              "id": "1552674277",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1552674277"
            },
            {
              "id": "1592955102",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1592955102"
            },
            {
              "id": "1562378160",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1562378160"
            },
            {
              "id": "1602189717",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1602189717"
            },
            {
              "id": "1565774887",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1565774887"
            },
            {
              "id": "1567856688",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1567856688"
            },
            {
              "id": "1559487505",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1559487505"
            },
            {
              "id": "1590799677",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1590799677"
            },
            {
              "id": "1548305659",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1548305659"
            },
            {
              "id": "1551734044",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1551734044"
            },
            {
              "id": "1554810806",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1554810806"
            }
          ]
        }
      }
    },
    {
      "id": "207195956",
      "type": "artists",
      "href": "/v1/catalog/us/artists/207195956",
      "attributes": {
        "genreNames": [
          "Classical"
        ],
        "url": "https://music.apple.com/us/artist/ola-gjeilo/207195956",
        "name": "Ola Gjeilo",
        "artwork": {
          "width": 979,
          "height": 979,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Features115/v4/e5/44/2b/e5442b89-557c-574d-6da2-0a41b21ee301/pr_source.png/{w}x{h}bb.jpg",
          "bgColor": "1a1f2c",
          "textColor1": "fcecec",
          "textColor2": "f3d9cd",
          "textColor3": "cfc3c5",
          "textColor4": "c7b4ac"
        }
      },
      "relationships": {
        "albums": {
          "href": "/v1/catalog/us/artists/207195956/albums",
          "data": [
            {
              "id": "1474949194",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1474949194"
            },
            {
              "id": "1440725489",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1440725489"
            },
            {
              "id": "1440792965",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1440792965"
            },
            {
              "id": "297130870",
              "type": "albums",
              "href": "/v1/catalog/us/albums/297130870"
            },
            {
              "id": "1584442069",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1584442069"
            },
            {
              "id": "518691931",
              "type": "albums",
              "href": "/v1/catalog/us/albums/518691931"
            },
            {
              "id": "1539403354",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1539403354"
            },
            {
              "id": "1597089042",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1597089042"
            },
            {
              "id": "1612738768",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1612738768"
            },
            {
              "id": "1596335391",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1596335391"
            },
            {
              "id": "1595646417",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1595646417"
            },
            {
              "id": "1610604513",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1610604513"
            },
            {
              "id": "1538083602",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1538083602"
            },
            {
              "id": "1556770248",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1556770248"
            },
            {
              "id": "1598634702",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1598634702"
            },
            {
              "id": "1594197526",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1594197526"
            },
            {
              "id": "1452314090",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1452314090"
            },
            {
              "id": "1599119969",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1599119969"
            },
            {
              "id": "1452290447",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1452290447"
            }
          ]
        }
      }
    },
    {
      "id": "1540549101",
      "type": "artists",
      "href": "/v1/catalog/us/artists/1540549101",
      "attributes": {
        "genreNames": [
          "Classical Crossover"
        ],
        "url": "https://music.apple.com/us/artist/eyd%C3%ADs-evensen/1540549101",
        "name": "Eydís Evensen",
        "artwork": {
          "width": 5406,
          "height": 5406,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/6f/da/c6/6fdac654-da38-2347-dc0d-52e97fd97e7e/pr_source.png/{w}x{h}bb.jpg",
          "bgColor": "333333",
          "textColor1": "ffffff",
          "textColor2": "e2e2e2",
          "textColor3": "d6d6d6",
          "textColor4": "bfbfbf"
        }
      },
      "relationships": {
        "albums": {
          "href": "/v1/catalog/us/artists/1540549101/albums",
          "data": [
            {
              "id": "1554074705",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1554074705"
            },
            {
              "id": "1613114680",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1613114680"
            },
            {
              "id": "1591874127",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1591874127"
            },
            {
              "id": "1551585603",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1551585603"
            },
            {
              "id": "1550204252",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1550204252"
            },
            {
              "id": "1611180072",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1611180072"
            },
            {
              "id": "1576152983",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1576152983"
            },
            {
              "id": "1569390938",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1569390938"
            },
            {
              "id": "1540549099",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1540549099"
            },
            {
              "id": "1582408719",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1582408719"
            },
            {
              "id": "1574162217",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1574162217"
            },
            {
              "id": "1589735393",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1589735393"
            },
            {
              "id": "1586581814",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1586581814"
            }
          ]
        }
      }
    },
    {
      "id": "912844864",
      "type": "artists",
      "href": "/v1/catalog/us/artists/912844864",
      "attributes": {
        "genreNames": [
          "Instrumental"
        ],
        "url": "https://music.apple.com/us/artist/hugar/912844864",
        "name": "Hugar",
        "artwork": {
          "width": 2919,
          "height": 2919,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Features125/v4/6c/c6/a4/6cc6a407-1bd9-ae82-4a63-c60b684c713f/pr_source.png/{w}x{h}bb.jpg",
          "bgColor": "141416",
          "textColor1": "d0d8d8",
          "textColor2": "d9c7c3",
          "textColor3": "aab1b1",
          "textColor4": "b1a3a0"
        }
      },
      "relationships": {
        "albums": {
          "href": "/v1/catalog/us/artists/912844864/albums",
          "data": [
            {
              "id": "1469866464",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1469866464"
            },
            {
              "id": "912844859",
              "type": "albums",
              "href": "/v1/catalog/us/albums/912844859"
            },
            {
              "id": "1593032344",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1593032344"
            },
            {
              "id": "1506572293",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1506572293"
            },
            {
              "id": "1558923270",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1558923270"
            },
            {
              "id": "1455072542",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1455072542"
            },
            {
              "id": "1539374205",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1539374205"
            },
            {
              "id": "1187479381",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1187479381"
            },
            {
              "id": "1600009270",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1600009270"
            },
            {
              "id": "1437774159",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1437774159"
            },
            {
              "id": "1181988538",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1181988538"
            },
            {
              "id": "1580382993",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1580382993"
            },
            {
              "id": "1411948068",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1411948068"
            },
            {
              "id": "1563679544",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1563679544"
            },
            {
              "id": "1587250186",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1587250186"
            },
            {
              "id": "1560604748",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1560604748"
            },
            {
              "id": "1552674482",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1552674482"
            },
            {
              "id": "1552674482",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1552674482"
            },
            {
              "id": "1558707316",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1558707316"
            },
            {
              "id": "1594150120",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1594150120"
            }
          ]
        }
      }
    },
    {
      "id": "265425550",
      "type": "artists",
      "href": "/v1/catalog/us/artists/265425550",
      "attributes": {
        "genreNames": [
          "Classical Crossover"
        ],
        "url": "https://music.apple.com/us/artist/%C3%B3lafur-arnalds/265425550",
        "name": "Ólafur Arnalds",
        "artwork": {
          "width": 1500,
          "height": 1500,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Features115/v4/a7/ee/3d/a7ee3d8d-9da3-915f-6c4f-27492b754663/mzl.bneuzttp.jpg/{w}x{h}bb.jpg",
          "bgColor": "dce0e9",
          "textColor1": "12100e",
          "textColor2": "242c30",
          "textColor3": "3b3a3a",
          "textColor4": "495055"
        }
      },
      "relationships": {
        "albums": {
          "href": "/v1/catalog/us/artists/265425550/albums",
          "next": "/v1/catalog/us/artists/265425550/albums?offset=25",
          "data": [
            {
              "id": "1390704147",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1390704147"
            },
            {
              "id": "1451058763",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451058763"
            },
            {
              "id": "1524005856",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1524005856"
            },
            {
              "id": "1440725037",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1440725037"
            },
            {
              "id": "1440723556",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1440723556"
            },
            {
              "id": "1440745149",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1440745149"
            },
            {
              "id": "1581805215",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1581805215"
            },
            {
              "id": "1440761769",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1440761769"
            },
            {
              "id": "1451076889",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451076889"
            },
            {
              "id": "1451076889",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451076889"
            },
            {
              "id": "1451185311",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451185311"
            },
            {
              "id": "1451167141",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451167141"
            },
            {
              "id": "1600268750",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1600268750"
            },
            {
              "id": "1451195241",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451195241"
            },
            {
              "id": "1440662390",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1440662390"
            },
            {
              "id": "1569200380",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1569200380"
            },
            {
              "id": "1451075286",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451075286"
            },
            {
              "id": "1451075286",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451075286"
            },
            {
              "id": "1451165438",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451165438"
            },
            {
              "id": "1451178606",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451178606"
            },
            {
              "id": "1106869077",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1106869077"
            },
            {
              "id": "1480052706",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1480052706"
            },
            {
              "id": "1508182008",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1508182008"
            },
            {
              "id": "1508182008",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1508182008"
            },
            {
              "id": "1508182008",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1508182008"
            }
          ]
        }
      }
    },
    {
      "id": "86250605",
      "type": "artists",
      "href": "/v1/catalog/us/artists/86250605",
      "attributes": {
        "genreNames": [
          "Ambient"
        ],
        "url": "https://music.apple.com/us/artist/nils-frahm/86250605",
        "name": "Nils Frahm",
        "artwork": {
          "width": 2652,
          "height": 2652,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/a1/a0/47/a1a0470a-0227-0ac6-7a76-0a0f0693d6b5/pr_source.png/{w}x{h}bb.jpg",
          "bgColor": "9c9e89",
          "textColor1": "0d0a09",
          "textColor2": "14110f",
          "textColor3": "2a2722",
          "textColor4": "2f2d28"
        }
      },
      "relationships": {
        "albums": {
          "href": "/v1/catalog/us/artists/86250605/albums",
          "next": "/v1/catalog/us/artists/86250605/albums?offset=25",
          "data": [
            {
              "id": "1451143439",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451143439"
            },
            {
              "id": "1504523483",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1504523483"
            },
            {
              "id": "1451159043",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451159043"
            },
            {
              "id": "1451056840",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451056840"
            },
            {
              "id": "1451076889",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451076889"
            },
            {
              "id": "1451076889",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451076889"
            },
            {
              "id": "1591461316",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1591461316"
            },
            {
              "id": "1536634309",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1536634309"
            },
            {
              "id": "1443975218",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1443975218"
            },
            {
              "id": "1475670331",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1475670331"
            },
            {
              "id": "1453571326",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1453571326"
            },
            {
              "id": "1451164610",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451164610"
            },
            {
              "id": "1553782903",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1553782903"
            },
            {
              "id": "1451150417",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451150417"
            },
            {
              "id": "1451075286",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451075286"
            },
            {
              "id": "1451075286",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451075286"
            },
            {
              "id": "1451167964",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451167964"
            },
            {
              "id": "1086159792",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1086159792"
            },
            {
              "id": "1451058868",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451058868"
            },
            {
              "id": "1451199167",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451199167"
            },
            {
              "id": "1451199167",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451199167"
            },
            {
              "id": "1451166665",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451166665"
            },
            {
              "id": "1451164642",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451164642"
            },
            {
              "id": "1451075515",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451075515"
            },
            {
              "id": "1451056931",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1451056931"
            }
          ]
        }
      }
    },
    {
      "id": "941440",
      "type": "artists",
      "href": "/v1/catalog/us/artists/941440",
      "attributes": {
        "genreNames": [
          "Classical Crossover"
        ],
        "url": "https://music.apple.com/us/artist/stephan-moccio/941440",
        "name": "Stephan Moccio",
        "artwork": {
          "width": 4480,
          "height": 4480,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/85/c8/c6/85c8c651-cb68-4e8a-9d5f-4c1a4e144b04/pr_source.png/{w}x{h}bb.jpg",
          "bgColor": "2d2d2f",
          "textColor1": "e6e0e5",
          "textColor2": "c7c293",
          "textColor3": "c1bcc1",
          "textColor4": "a8a47f"
        }
      },
      "relationships": {
        "albums": {
          "href": "/v1/catalog/us/artists/941440/albums",
          "next": "/v1/catalog/us/artists/941440/albums?offset=25",
          "data": [
            {
              "id": "1579486164",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1579486164"
            },
            {
              "id": "1521874082",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1521874082"
            },
            {
              "id": "1610585907",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1610585907"
            },
            {
              "id": "1535928022",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1535928022"
            },
            {
              "id": "1596708807",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1596708807"
            },
            {
              "id": "1596708807",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1596708807"
            },
            {
              "id": "969109364",
              "type": "albums",
              "href": "/v1/catalog/us/albums/969109364"
            },
            {
              "id": "1571678099",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1571678099"
            },
            {
              "id": "1550089749",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1550089749"
            },
            {
              "id": "1563224095",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1563224095"
            },
            {
              "id": "1567147461",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1567147461"
            },
            {
              "id": "1597789025",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1597789025"
            },
            {
              "id": "1598102960",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1598102960"
            },
            {
              "id": "1558001677",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1558001677"
            },
            {
              "id": "1506107847",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1506107847"
            },
            {
              "id": "1553384815",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1553384815"
            },
            {
              "id": "1577352994",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1577352994"
            },
            {
              "id": "1559090459",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1559090459"
            },
            {
              "id": "1511907224",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1511907224"
            },
            {
              "id": "1552197550",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1552197550"
            },
            {
              "id": "1585383919",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1585383919"
            },
            {
              "id": "1538901112",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1538901112"
            },
            {
              "id": "1516612538",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1516612538"
            },
            {
              "id": "1604239561",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1604239561"
            },
            {
              "id": "1569753851",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1569753851"
            }
          ]
        }
      }
    },
    {
      "id": "1172931586",
      "type": "artists",
      "href": "/v1/catalog/us/artists/1172931586",
      "attributes": {
        "genreNames": [
          "Classical"
        ],
        "url": "https://music.apple.com/us/artist/olivia-belli/1172931586",
        "name": "Olivia Belli",
        "artwork": {
          "width": 800,
          "height": 800,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Music124/v4/a8/4c/9d/a84c9d17-216a-2437-713a-d749d01502aa/pr_source.png/{w}x{h}bb.jpg",
          "bgColor": "4b5b6e",
          "textColor1": "f6f8e5",
          "textColor2": "ecf7e5",
          "textColor3": "d4d8cd",
          "textColor4": "ccd8cd"
        }
      },
      "relationships": {
        "albums": {
          "href": "/v1/catalog/us/artists/1172931586/albums",
          "next": "/v1/catalog/us/artists/1172931586/albums?offset=25",
          "data": [
            {
              "id": "1570081970",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1570081970"
            },
            {
              "id": "1447380116",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1447380116"
            },
            {
              "id": "1272475615",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1272475615"
            },
            {
              "id": "1317038890",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1317038890"
            },
            {
              "id": "1473457365",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1473457365"
            },
            {
              "id": "1590799978",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1590799978"
            },
            {
              "id": "1609686256",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1609686256"
            },
            {
              "id": "1366002528",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1366002528"
            },
            {
              "id": "1563679334",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1563679334"
            },
            {
              "id": "1499018332",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1499018332"
            },
            {
              "id": "1542328745",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1542328745"
            },
            {
              "id": "1609730789",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1609730789"
            },
            {
              "id": "1610971866",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1610971866"
            },
            {
              "id": "1502728339",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1502728339"
            },
            {
              "id": "1290864597",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1290864597"
            },
            {
              "id": "1304356341",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1304356341"
            },
            {
              "id": "1450503504",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1450503504"
            },
            {
              "id": "1560605346",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1560605346"
            },
            {
              "id": "1614196584",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1614196584"
            },
            {
              "id": "1537033215",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1537033215"
            },
            {
              "id": "1462460250",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1462460250"
            },
            {
              "id": "1204880079",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1204880079"
            },
            {
              "id": "1444605999",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1444605999"
            },
            {
              "id": "1608414283",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1608414283"
            },
            {
              "id": "1581367194",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1581367194"
            }
          ]
        }
      }
    }
  ]
}
```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/playlists/{id}/view/{view}`

## Parameters

- `extend` ([string]): A list of attribute extensions to apply to resources in the response.
- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `with` ([string]): A list of modifications to apply to the request.

## See Also

- [object Playlists](playlists.md)
  A resource object that represents a playlist.
- [object PlaylistsResponse](playlistsresponse.md)
  The response to a playlists request.
- [Get a Catalog Playlist](get-a-catalog-playlist.md)
  Fetch a playlist by using its identifier.
- [Get a Catalog Playlist's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-707nb.md)
  Fetch a playlist’s relationship by using its identifier.
- [Get Multiple Catalog Playlists](get-multiple-catalog-playlists.md)
  Fetch one or more playlists by using their identifiers.
- [Get Charts Playlists by Storefront Value](get-charts-playlists-by-storefront-value.md)
  Fetch one or more Charts Playlists by using their Storefront value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/fetch-a-view-on-this-resource-by-name-6i3ek)*